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
	return lrModel.coef_, lrModel.intercept_

def test(scoreList, coef_, intercept_):
	# Init 
	lrModel = linear_model.LogisticRegression()
	lrModel.coef_ = coef_
	lrModel.intercept_ = intercept_
	prob = lrModel.predict_proba(preprocessing.normalize(scoreList))[1]
	apkScore = "%.2f" % (prob*100)
	return apkScore