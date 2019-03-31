#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import numpy as np
import Reader as re
import time

import Sobel as sob
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


accuracy_bayes_h=0
accuracy_ada_h=0
accuracy_svm_h=0
accuracy_bayes_s=0
accuracy_ada_s=0
accuracy_svm_s=0
tmp_accracy_bayes_h=0
tmp_accracy_ada_h=0
tmp_accracy_svm_h=0
tmp_accracy_bayes_s=0
tmp_accracy_ada_s=0
tmp_accracy_svm_s=0
accuracy=0

if(pathTrain is not None):
    #data,target = re.dataHistogramme(pathTrain)
    #data2,target2 = sob.dataSobel(pathTrain)
    #SobelHistogrammeData=np.concatenate((data2,data),axis = 1)
    #ada.ada_boostParam(data,target)
    #svm.svmModelParam(SobelHistogrammeData,target)
    tmps1=time.clock()
    nbIter=0
    Dataname, targetName=re.NameTarget(pathTrain)
    for i in range(5): #Moyenne de i iteration
        print("-- test",nbIter,"start --")
        tmpsL=time.clock()
        X_train, X_test, y_train, y_test = train_test_split(Dataname, targetName, train_size=0.8, test_size=0.2)
        X_Histo_train=re.getHistogramme(X_train)
        X_Sobel_train=sob.getSobel(X_train)
        #X_Sobel_train=sob.getFastSobel(X_train)
        X_Histo_test=re.getHistogramme(X_test)
        X_Sobel_test=sob.getSobel(X_test)
        #X_Sobel_test=sob.getFastSobel(X_test)
        tmps2=time.clock()
        print("Learning time : " ,round((tmps2-tmpsL),4),'sec\n')
        #print("X_train : ",X_train.shape)
        #print("X_test : ",X_test.shape)
        #print("y_train : ",y_train.shape)
        #print("y_test : ",y_test.shape)
        #print("X_train histo : ", X_Histo_train.shape)
        #print("X_train sobel : ", X_Sobel_train.shape)
        #exit()
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
        tmp_accracy_bayes_h = accuracy_score(accuracy_bayes_Histo,y_test)
        tmp_accracy_ada_h = accuracy_score(accuracy_ada_Histo,y_test)
        tmp_accracy_svm_h = accuracy_score(accuracy_svm_Histo,y_test)
        tmp_accracy_bayes_s = accuracy_score(accuracy_bayes_Sobel,y_test)
        tmp_accracy_ada_s = accuracy_score(accuracy_ada_Sobel,y_test)
        tmp_accracy_svm_s = accuracy_score(accuracy_svm_Sobel,y_test)

        vector = [accuracy_bayes_Histo*(tmp_accracy_bayes_h),
                  accuracy_ada_Histo*(tmp_accracy_ada_h),
                  accuracy_svm_Histo*(tmp_accracy_svm_h),
                  accuracy_bayes_Sobel*(tmp_accracy_bayes_s),
                  accuracy_ada_Sobel*(tmp_accracy_ada_s),
                  accuracy_svm_Sobel*(tmp_accracy_svm_s)]

        print('\n')
        for i in range(len(vector)):
            print(vector[i],'\n')
        voteResult=moy.Votes(vector)
        accuracy+=accuracy_score(voteResult, y_test)
        nbIter+=1

        print("bayes_Histo : ",tmp_accracy_bayes_h)
        print("ada_Histo : ",tmp_accracy_ada_h)
        print("SVM_Histo : ",tmp_accracy_svm_h)
        print("bayes_Sobel : ",tmp_accracy_bayes_s)
        print("ada_Sobel : ",tmp_accracy_ada_s)
        print("svm_Sobel : ",tmp_accracy_svm_s)
        #print("bagging : ",accuracy_score(accuracy_bagging,y_test))
        accuracy_bayes_h += tmp_accracy_bayes_h
        accuracy_ada_h += tmp_accracy_ada_h
        accuracy_svm_h += tmp_accracy_svm_h
        accuracy_bayes_s += tmp_accracy_bayes_s
        accuracy_ada_s += tmp_accracy_ada_s
        accuracy_svm_s += tmp_accracy_svm_s
        print("Vote test",nbIter,": ",accuracy_score(voteResult, y_test),'\n')
        tmps3=time.clock()
        print("Execution time : " ,round((tmps3-tmps2),4),'sec\n')

    print("---------------------------------------------")
    print("bayes_Histo average : ",accuracy_bayes_h/nbIter)
    print("ada_Histo average : ",accuracy_ada_h/nbIter)
    print("SVM_Histo average : ",accuracy_svm_h/nbIter)
    print("bayes_Sobel average : ",accuracy_bayes_s/nbIter)
    print("ada_Sobel average : ",accuracy_ada_s/nbIter)
    print("SVM_Sobel average : ",accuracy_svm_s/nbIter)
    print("Average of votes = ",accuracy/nbIter)
    tmpsF=time.clock()
    print("Final execution time : " ,round((tmpsF-tmps1),4),'sec\n')


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
    #print(vector)
    voteResult=moy.Votes(vector)
    for i in range(len(vector)):
        print(vector[i],'\n')

    JsonOut.outPutJson(fileList, pathPredict, voteResult)
