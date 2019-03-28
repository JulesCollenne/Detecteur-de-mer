#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

def outPutJson(image,result):
    d = {}
    for i in range(len(image)):
        d[image[i]] = int(result[i])
        print(json.dumps(d, ensure_ascii=False))
        
    with open('data.txt', 'w') as outfile:  
        json.dump(d, outfile)
    
#outPutJson(["eza","salut"],[2,3])