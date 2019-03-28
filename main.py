#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import Reader as re
import Images.DataGetter as dg
import OutputJson as jout


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
    print("Demarrage")
    #data,target =sob.SobelImage(pathTrain)
    data,target=re.dataHistogramme(pathTrain)
    print ("Lancement de l'apprentissage. Allez vous faire un cafe !")
    for _ in range(1):          
        accuracy_bayes += bayes.Bayes(data,target)        
      #  accuracy_ada += ada.ada_boost(data, target)
        print("Merci de patienter.")
    print("Bayses = ", accuracy_bayes/1)
    #print("AdaBoost = ", accuracy_ada/1)
    
    
    
    
if(pathPredict is not None):
    data,nameFiles = re.dataHistogrammePredict(pathPredict)
    result=model.load_Model('Bayes.sav', data)
    print(result)
    jout.outPutJson(nameFiles,result)
    
    
    
