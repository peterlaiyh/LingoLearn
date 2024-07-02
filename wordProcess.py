#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 01:29:45 2023

@author: peterlai
"""

import pandas as pd


def writeRawWord(filename="raw.txt"):
    wordList = []
    while(True):
        word = input("Please enter the word you would like to look up later.(Input 9999 to end.)\n")
        if word == "9999":
            break
        wordList.append(word)
    if not ".txt" in filename: 
        filename += ".txt"
    with open(filename, 'w') as file_object:
        for word in wordList:
            file_object.write(word+"\n")
            
def readRawWord(filename="raw.txt"):
    if not ".txt" in filename: 
        filename += ".txt"
    try:
        with open(filename, 'r') as file_object:
            wordList = file_object.read().split("\n")
            if len(wordList)>1:
                wordList.pop()
    except FileNotFoundError:
        print("File Not Found.")
    else:
        return(wordList)
    
def writeNote(df,e2jName="e2j.csv",j2eName="j2e.csv"):
    if not ".csv" in e2jName: 
        e2jName += ".csv"
    if not ".csv" in j2eName: 
        j2eName += ".csv"   
    df1New = df[df["Language"]=="e2j"].drop(columns=("Language"))
    try:
        df1 = pd.read_csv(e2jName)
    except FileNotFoundError:
        df1 = df1New
    else:
        df1 = pd.concat([df1,df1New],ignore_index=True).drop_duplicates(subset=["Word"],keep="last")
    df1.to_csv(e2jName,encoding="utf_8_sig",index=False)
    
    df2New = df[df["Language"]=="j2e"].drop(columns=("Language"))
    try:
        df2 = pd.read_csv(j2eName)
    except FileNotFoundError:
        df2 = df2New
    else:
        df2 = pd.concat([df2,df2New],ignore_index=True).drop_duplicates(subset=["Word"],keep="last")
    df2.to_csv(j2eName,encoding="utf_8_sig",index=False)