#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

def outPutJson(image,result):
    d = {}
    for i in range(len(image)):
        d[image[i]] = str(int(result[i]))
        
    with open('result.json', 'w') as outfile:  
        json.dump(d, outfile,indent=4)
        outfile.write("\n")
#outPutJson(["eza","salut"],[2,3])