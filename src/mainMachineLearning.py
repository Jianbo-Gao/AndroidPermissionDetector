#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Main Machine Learning

from numpy import *
import ConfigParser, os, json
import xmlExtracter, xmlParser, logRegression, listReas



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
			if apkDirPath.endswith("/"):
				apkPath = apkDirPath+apk
			else:
				apkPath = apkDirPath + "/" + apk
			xmlString = xmlExtracter.extract(apkPath)
			apkPermissionsList.append(xmlParser.parseString(xmlString))

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

	def _calculateApkScoreList(self, permissionsScoreDict, apkPermissionsList):
		apkScoreList = []
		for apkPermissions in apkPermissionsList:
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
			apkScoreList.append([rScore,eScore,aScore,sScore])
		return apkScoreList

	def _calculateReasScoreList(self, apkScoreList):
		reasScoreList = []
		for score in apkScoreList:
			r = score[0]
			e = score[1]
			a = score[2]
			s = score[3]
			reasScoreList.append([1.0, r*e, e, r*a*s, a*s])
		return reasScoreList

	# use Google samples and Malware samples
	def train(self, googleDirPath, malwareDirPath, numIter, gui):

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
		labelList = hstack((ones(googleLen), zeros(malwareLen)))

		return logRegression.smoothStocGradAscent(mat(apkScoreList), labelList.transpose(), numIter, gui)

