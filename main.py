#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import Reader as re

import Test as sob
import Algorithm.bayes as bayes
import Algorithm.ada_boost as ada
import Algorithm.Model as model
import Algorithm.svm as svm
import Moyenne as moy
import OutputJson as JsonOut
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


ap=argparse.ArgumentParser()
ap.add_argument("-f","--fit",required= False, help="Path to Data Folder")
ap.add_argument("-p","--predict",required=False, help="Path to Data Folder")
args=vars(ap.parse_args())

pathTrain=args["fit"]
pathPredict=args["predict"]


accuracy_bayes = []
accuracy_ada = []
accuracy_svm=[]
accuracy=0
if(pathTrain is not None):   
    data,target = sob.trueSobel(pathTrain)
    data2,target2 = sob.dataSobel(pathTrain)
    print ("DATA TRY : ",data.shape)
    print ("DATA WORKING : ",data2.shape)
    print ("TARGET TRY : ",target.shape)
    print ("TARGER WORKING : ",target2.shape)
    if(data.shape==data2.shape):
        print("DATA OK")
    else:
        print("DATA PAS OK")
    if(target.shape==target2.shape):
        print("TARGET OK")
    else:
        print("TARGET PAS OK")
        
    
    X_train, X_test, y_train, y_test = train_test_split(data, target, train_size=0.8, test_size=0.2)
    nbIter=0
    for i in range(50):
        print(nbIter," start")
        accuracy_bayes = bayes.Bayes(X_train, X_test, y_train, y_test)     
        accuracy_ada  = ada.ada_boost(X_train, X_test, y_train, y_test)
        accuracy_svm   = svm.svmModel(X_train, X_test, y_train, y_test)
        vector = [accuracy_bayes, accuracy_ada, accuracy_svm]
        voteResult=moy.Votes(vector)
        accuracy+=accuracy_score(y_test, voteResult)
        nbIter+=1
        
        
        
        
    #print("Bayses = ", accuracy_bayes/20)
    #print("AdaBoost = ", accuracy_ada/20)
    #print("Svm = ", accuracy_svm/20)
    print(accuracy/nbIter)
    
    
if(pathPredict is not None):
    data,fileList =sob.trueSobelPredict(pathPredict)
    resultBayes=model.load_Model('Bayes.sav',data)
    resultAda=model.load_Model('AdaBoost.sav',data)
    vector=[resultBayes,resultAda]
    voteResult=moy.Votes(vector)
    print (voteResult)
    JsonOut.outPutJson(fileList,resultBayes)
