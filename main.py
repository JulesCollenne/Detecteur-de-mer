#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import Reader as re
import Algorithm.bayes as alg
import Algorithm.ada_boost as alg2


ap=argparse.ArgumentParser()
ap.add_argument("-t","--train",required= False, help="Path to Data Folder")
ap.add_argument("-p","--predict",required=False, help="Path to Data Folder")
args=vars(ap.parse_args())

pathTrain=args["train"]
pathPredict=args["predict"]

accuracy = 0
if(pathTrain is not None):
    
    for _ in range(20):  
        data,target =re.dataHistogramme(pathTrain)
        #print(alg.Bayses(data,target))
        accuracy += alg.Bayses(data,target)
        #print(alg2.ada_boost(data, target))
        #accuracy += alg2.ada_boost(data, target)
    print("acc = ", accuracy/20)
    
    
    
if(pathPredict is not None):
    pass
    #predict() to do
    
