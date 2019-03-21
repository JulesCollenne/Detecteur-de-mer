#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import Reader as re



import Test as sob

import Algorithm.bayes as bayes
import Algorithm.ada_boost as ada
import Algorithm.Model as model

ap=argparse.ArgumentParser()
ap.add_argument("-f","--fit",required= False, help="Path to Data Folder")
ap.add_argument("-p","--predict",required=False, help="Path to Data Folder")
args=vars(ap.parse_args())

pathTrain=args["fit"]
pathPredict=args["predict"]


accuracy_bayes = 0
accuracy_ada = 0

if(pathTrain is not None):    
    data,target =re.dataHistogramme(pathTrain)
    for _ in range(20):          
        accuracy_bayes += bayes.Bayes(data,target)        
        accuracy_ada += ada.ada_boost(data, target)
    print("Bayses = ", accuracy_bayes/20)
    print("AdaBoost = ", accuracy_ada/20)
    
    
    
if(pathPredict is not None):
    print("Bayses loaded = "+str(model.load_Model('Bayes.sav', pathPredict)))
    print("AdaBoost loaded = "+str(model.load_Model('AdaBoost.sav', pathPredict)))
    
