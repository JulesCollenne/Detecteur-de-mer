#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import Reader as re
from sklearn.model_selection import train_test_split # version 0.18.1
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


ap=argparse.ArgumentParser()
ap.add_argument("-t","--train",required= False, help="Path to Data Folder")
ap.add_argument("-p","--predict",required=False, help="Path to Data Folder")
args=vars(ap.parse_args())

pathTrain=args["train"]
pathPredict=args["predict"]

if(pathTrain is not None):
    data,target =re.dataHistogramme(pathTrain)
    data_test = train_test_split(data, target
                                 , random_state=0
                                 , train_size=0.5)
    data_train, data_test, target_train, target_test = data_test
    #print(data_train)
    #print(target_train.shape)
    
    #train
    clf = GaussianNB()
    clf.fit(data_train, target_train)
    #predict
    result = clf.predict(data_test)
    #score
    print(accuracy_score(result, target_test))
    #train() to do
    
if(pathPredict is not None):
    pass
    #predict() to do
    
