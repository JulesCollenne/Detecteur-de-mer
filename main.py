#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse

ap=argparse.ArgumentParser()
ap.add_argument("-t","--train",required= False, help="Path to Data Folder")
ap.add_argument("-p","--predict",required=False, help="Path to Data Folder")
args=vars(ap.parse_args())

pathTrain=args["train"]
pathPredict=args["predict"]

print(pathTrain)
print(pathPredict)




if(pathTrain is not None):
    pass
    #train() to do
if(pathPredict is not None):
    pass
    #predict() to do
    
