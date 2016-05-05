#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Main Machine Learning

from numpy import *
import os, json
import xmlExtracter, xmlParser, logRegression, listReas, log

class MachineLearning:

	def __init__(self):
		# init reasPermissionsList
		reas = listReas.ListReas()
		self.reasPermissionsList = reas.getReasList()
		self.rPermissionsList = reas.getRList()
		self.ePermissionsList = reas.getEList()
		self.aPermissionsList = reas.getAList()
		self.sPermissionsList = reas.getSList()



	def _loadPermissions(self, apkDirPath):

		# get permissions for all apk files.
		apkPermissionsList = []
		for apk in os.listdir(apkDirPath):
			if not apk.endswith(".apk"):
				continue
			apkPath = os.path.join(apkDirPath, apk)
			xmlString = xmlExtracter.extract(apkPath)
			if xmlString:
				apkPermissions = xmlParser.parseString(xmlString)
				if apkPermissions:
					apkPermissionsList.append(apkPermissions)

		# delete useless permissions.
		# calculate sum of every permission in R, E, A, S.
		reasPermissionsSumDict = {}
		for reasPermission in self.reasPermissionsList:
			reasPermissionsSumDict[reasPermission] = 0

		for permissionsList in apkPermissionsList:
			for permission in permissionsList:
				if reasPermissionsSumDict.has_key(permission):
					reasPermissionsSumDict[permission] += 1
				else:
					permissionsList.remove(permission)
		return apkPermissionsList, reasPermissionsSumDict

	def _calculateApkScore(self, permissionsScoreDict, apkPermissions):
		rScore = eScore = aScore = sScore = 0.0
		for permission in apkPermissions:
			if permission in self.rPermissionsList:
				rScore += permissionsScoreDict[permission]
			if permission in self.ePermissionsList:
				eScore += permissionsScoreDict[permission]
			if permission in self.aPermissionsList:
				aScore += permissionsScoreDict[permission]
			if permission in self.sPermissionsList:
				sScore += permissionsScoreDict[permission]
		return [rScore,eScore,aScore,sScore]

	def _calculateApkScoreList(self, permissionsScoreDict, apkPermissionsList):
		apkScoreList = []
		for apkPermissions in apkPermissionsList:
			apkScoreList.append(self._calculateApkScore(permissionsScoreDict, apkPermissions))
		return apkScoreList

	def _calculateReasScore(self, score):
		r = (score[0] if score[0] > 0 else 0)
		e = (score[1] if score[1] > 0 else 0)
		a = (score[2] if score[2] > 0 else 0)
		s = (score[3] if score[3] > 0 else 0)
		reScore = (-r*e if (score[0]<0 or score[1]<0) else r*e)
		rasScore = (-r*a*s if (score[0]<0 or score[2]<0 or score[3]<0) else r*a*s)
		asScore = (-a*s if (score[2]<0 or score[3]<0) else a*s)
		return [1.0, reScore, e, rasScore, asScore]

	def _calculateReasScoreList(self, apkScoreList):
		reasScoreList = []
		for score in apkScoreList:
			reasScoreList.append(self._calculateReasScore(score))
		return reasScoreList

	# use Google samples and Malware samples
	def train(self, googleDirPath, malwareDirPath, paramFilePath=None, numIter=200, alphaLen=50, gui=False):

		if not os.path.isdir(googleDirPath):
			log.error("no such google dir")
			exit()
		if not os.path.isdir(malwareDirPath):
			log.error("no such malware dir")
			exit()

		# get google and malware permissionsList and reasPermissionsSumDict
		googleApkPermissionsList, googleReasPermissionsSumDict = self._loadPermissions(googleDirPath)
		malwareApkPermissionsList, malwareReasPermissionsSumDict = self._loadPermissions(malwareDirPath)

		# calculate score for every permission
		permissionsScoreDict = {}
		for permission in self.reasPermissionsList:
			permissionsScoreDict[permission] = malwareReasPermissionsSumDict[permission] - googleReasPermissionsSumDict[permission]

		# calculate score for every apk file
		# every tuple includes rScore, eScore, aScore, sScore
		googleApkScoreList = self._calculateApkScoreList(permissionsScoreDict, googleApkPermissionsList)
		malwareApkScoreList = self._calculateApkScoreList(permissionsScoreDict, malwareApkPermissionsList)

		# calculate reas score for every apk file
		# every tuple includes 1.0(constant), combinations of rScore, eScore, aScore, sScore
		googleReasScoreList = self._calculateReasScoreList(googleApkScoreList)
		malwareReasScoreList = self._calculateReasScoreList(malwareApkScoreList)

		# init mat for logRegression
		apkScoreList = googleReasScoreList + malwareReasScoreList
		googleLen = len(googleReasScoreList)
		malwareLen = len(malwareReasScoreList)
		labelList = hstack((zeros(googleLen), ones(malwareLen)))

		weights = logRegression.smoothStocGradAscent(mat(apkScoreList), labelList.transpose(), numIter, alphaLen, gui)
		weightsList = weights.transpose().tolist()[0]

		params = {}
		params['weights'] = weightsList
		params['permissions'] = permissionsScoreDict
		params['googleNum'] = googleLen
		params['malwareNum'] = malwareLen
		paramsJson = json.dumps(params)

		# write params into paramFile
		if paramFilePath != None:
			try:
				paramFile = open(paramFilePath, 'w')
				paramFile.write(paramsJson)
				paramFile.close()
			except Exception, e:
				log.error("write params into paramFile failed.")

		return paramsJson

	# test apk file using param
	def test(self, testApkFilePath, paramFilePath):
		if not os.path.isfile(testApkFilePath):
			log.error("no such apk file.")
			exit()
		if not os.path.isfile(paramFilePath):
			log.error("no such param file.")
			exit()

		xmlString = xmlExtracter.extract(testApkFilePath)
		permissionsList = xmlParser.parseString(xmlString)

		# read params
		try:
			paramFile = open(paramFilePath, 'r')
			paramsJson = paramFile.readline()
			paramFile.close()
		except Exception, e:
			log.error("can not read params")
			return
		try:
			params = json.loads(paramsJson)
		except Exception, e:
			log.error("params type error.")
			return

		# test method
		permissions = params['permissions']
		weights = params['weights']
		apkScoreList = self._calculateApkScore(permissions, permissionsList)
		reasScoreList = self._calculateReasScore(apkScoreList)
		weightsMat = mat(weights)
		reasScoreMat = mat(reasScoreList).transpose()
		testScoreMat = weightsMat * reasScoreMat
		testScore = testScoreMat[0,0]
		logRegressionScore = 1.0/(1+exp(-testScore))

		return logRegressionScore

