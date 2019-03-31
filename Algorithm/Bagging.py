#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
def baggingModel(X_train, X_test, y_train, y_test):
    bagging= BaggingClassifier(KNeighborsClassifier(),max_samples=0.5,max_features=0.5)
    bagging.fit(X_train,y_train)
    y_predict = bagging.predict(X_test)
    return y_predict
