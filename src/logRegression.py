#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# @author: Garfy
# Logistic Regression

from sklearn import preprocessing, linear_model
from numpy import *
import log


def train(scoreList, labelList):
	# Mat
	scoreMat = mat(scoreList)

	# Normalize data
	normalizedScoreMat = preprocessing.normalize(scoreMat)

	# Logistic Regression
	lrModel = linear_model.LogisticRegression()
	lrModel.fit(normalizedScoreMat, labelList)

	# Return params
	return lrModel.coef_.tolist(), lrModel.intercept_.tolist()

def test(scoreList, coef_, intercept_):
	# Init: transform array to numpy.ndarray and load params
	lrModel = linear_model.LogisticRegression()
	lrModel.coef_ = ndarray(shape=(1,5), dtype=float, buffer=array(coef_))
	lrModel.intercept_ = ndarray(shape=(1,), dtype=float, buffer=array(intercept_))

	# Calculate Control power
	prob = lrModel.predict_proba(preprocessing.normalize([scoreList]))[0][1]
	apkScore = "%.2f" % (prob*100)
	return apkScore