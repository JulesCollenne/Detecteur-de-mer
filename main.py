#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import Reader as re
import Algorithm.bayes as alg


ap=argparse.ArgumentParser()
ap.add_argument("-t","--train",required= False, help="Path to Data Folder")
ap.add_argument("-p","--predict",required=False, help="Path to Data Folder")
args=vars(ap.parse_args())

pathTrain=args["train"]
pathPredict=args["predict"]

if(pathTrain is not None):
    data,target =re.dataHistogramme(pathTrain)
    alg.Bayses(data,target)
    
if(pathPredict is not None):
    pass
    #predict() to do
    
