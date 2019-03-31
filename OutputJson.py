#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json

def outPutJson(imgPathList, dirPath, result):
    d = {}

    for i in range(len(imgPathList)):
        imgPathList[i] = imgPathList[i].replace(dirPath+'/', '')

    for i in range(len(imgPathList)):
        d[imgPathList[i]] = int(result[i])

    with open('result.json', 'w') as outfile:
        json.dump(d, outfile,indent=4)
        outfile.write("\n")
#outPutJson(["eza","salut"],[2,3])
