#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import numpy as np
import Reader as re

import Test as sob
import Algorithm.bayes as bayes
import Algorithm.ada_boost as ada
import Algorithm.Model as model
import Algorithm.svm as svm
import Algorithm.Bagging as bag
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
    #data,target = re.dataHistogramme(pathTrain)
    #data2,target2 = sob.dataSobel(pathTrain)
    #SobelHistogrammeData=np.concatenate((data2,data),axis = 1)
    #ada.ada_boostParam(data,target)
    #svm.svmModelParam(SobelHistogrammeData,target)
    nbIter=0
    Dataname, targetName=re.NameTarget(pathTrain)
    for i in range(5): #Moyenne de i iteration
        print(nbIter," start")
        X_train, X_test, y_train, y_test = train_test_split(Dataname, targetName, train_size=0.8, test_size=0.2)
        X_Histo_train=re.getHistogramme(X_train)
        X_Sobel_train=sob.getSobel(X_train)
        X_Histo_test=re.getHistogramme(X_test)
        X_Sobel_test=sob.getSobel(X_test)
        #print(X_train.shape)
        #print("X_train : ",X_Histo_train.shape)
        #print("X_test : ",X_Histo_test.shape)
        #print("y_train : ",y_train.shape)
        #print("y_test : ",y_test.shape)
        print('bayes_Histo')
        accuracy_bayes_Histo = bayes.BayesHisto(X_Histo_train, X_Histo_test, y_train, y_test)
        print('ada_Histo')
        accuracy_ada_Histo  = ada.ada_boostHistogramme(X_Histo_train, X_Histo_test, y_train, y_test)
        print('svm_Histo')
        accuracy_svm_Histo   = svm.svmModelHistogramme(X_Histo_train, X_Histo_test, y_train, y_test)
        print('bayes_Sobel')
        accuracy_bayes_Sobel = bayes.BayesSobel(X_Sobel_train, X_Sobel_test, y_train, y_test)
        print('ada_Sobel')
        accuracy_ada_Sobel  = ada.ada_boostDataSobel(X_Sobel_train, X_Sobel_test, y_train, y_test)
        print('svm_Sobel')
        accuracy_svm_Sobel   = svm.svmModelDataSobel(X_Sobel_train, X_Sobel_test, y_train, y_test)
        #print('bagging')
        #accuracy_bagging=bag.baggingModel(X_train, X_test, y_train, y_test)
        vector = [accuracy_bayes_Histo*(accuracy_score(accuracy_bayes_Histo,y_test)/100),
                  accuracy_ada_Histo*(accuracy_score(accuracy_ada_Histo,y_test)/100),
                  accuracy_svm_Histo*(accuracy_score(accuracy_svm_Histo,y_test)/100),
                  accuracy_bayes_Sobel*(accuracy_score(accuracy_bayes_Sobel,y_test)/100),
                  accuracy_ada_Sobel*(accuracy_score(accuracy_ada_Sobel,y_test)/100),
                  accuracy_svm_Sobel*(accuracy_score(accuracy_svm_Sobel,y_test)/100)]
        print(vector)
        voteResult=moy.Votes(vector)
        accuracy+=accuracy_score(voteResult, y_test)
        nbIter+=1
        print("bayes_Histo : ",accuracy_score(accuracy_bayes_Histo,y_test))
        print("ada_Histo : ",accuracy_score(accuracy_ada_Histo,y_test))
        print("SVM_Histo : ",accuracy_score(accuracy_svm_Histo,y_test))
        print("bayes_Sobel : ",accuracy_score(accuracy_bayes_Sobel,y_test))
        print("ada_Sobel : ",accuracy_score(accuracy_ada_Sobel,y_test))
        print("SVM_Sobel : ",accuracy_score(accuracy_svm_Sobel,y_test))
        #print("bagging : ",accuracy_score(accuracy_bagging,y_test))
        print("Vote : ",accuracy_score(voteResult, y_test))
   
        
        
    #print("Bayses = ", accuracy_bayes/20)
    #print("AdaBoost = ", accuracy_ada/20)
    #print("Svm = ", accuracy_svm/20)
    print("vote Moyenne = ",accuracy/nbIter)
    
    
if(pathPredict is not None):
    dataSobel,fileList =sob.dataSobelPredict(pathPredict)
    dataHisto, fileList2= re.dataHistogrammePredict(pathPredict)
    #dataHisto, fileList =re.
    resultBayesSobel=model.load_Model('BayesSobel.sav',dataSobel)
    resultAdaSobel=model.load_Model('AdaBoostSobel.sav',dataSobel)
    resultSvmSobel=model.load_Model('svmSobel.sav',dataSobel)
    resultBayesHisto=model.load_Model('BayesHisto.sav',dataHisto)
    resultAdaHisto=model.load_Model('AdaBoostHisto.sav',dataHisto)
    resultSvmHisto=model.load_Model('svmHisto.sav',dataHisto)
    vector=[resultBayesSobel,resultAdaSobel,resultSvmSobel,resultBayesHisto,resultAdaHisto,resultSvmHisto]
    print(vector)
    voteResult=moy.Votes(vector)
    #print (voteResult)
    JsonOut.outPutJson(fileList,voteResult)
