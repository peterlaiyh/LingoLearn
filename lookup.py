#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 11:42:27 2023

@author: peterlai
"""

from bs4 import BeautifulSoup
import requests
from pandas import DataFrame
from common import wordChangeForm


def e2j(word):
    result = requests.get("http://ejje.weblio.jp/content/"+word)
    html = BeautifulSoup(result.text, 'html.parser')
    meaning = html.find(class_="content-explanation")
    if meaning:
        meaning = meaning.getText().strip()
    else:
        meaning = "NO RESULT"
    pron = html.find(class_="phoneticEjjeDesc")        
    if pron:
            pron = pron.getText().strip()
    else:
        if " " in word:
            pron = ""
            seperateWord = word.split(" ")
            for each in seperateWord:
                eachResult = requests.get("http://ejje.weblio.jp/content/"+each)
                eachHtml = BeautifulSoup(eachResult.text, 'html.parser')
                pron += eachHtml.find(class_="phoneticEjjeDesc").getText().strip()+" "
            pron = pron.rstrip()
        else:
            pron = "NO RESULT"

    return["e2j",word,pron,meaning]

                
def j2e(word):
    result = requests.get("http://ejje.weblio.jp/content/"+word)
    html = BeautifulSoup(result.text, 'html.parser')
    meaning = html.find(class_="content-explanation je")
    if meaning:
        meaning = meaning.getText().strip()
    else:
        meaning = "NO RESULT"
    pron = html.find(class_="ruby")
    if pron:
        pron = wordChangeForm(pron.getText().strip())
    else:
        if meaning:
            pron = wordChangeForm(word)
        else:
            pron = "NO RESULT"
    pron = pron.replace("‐","")
    return["j2e",word,pron,meaning]
            

def lookupSingle(word):
    for ch in word:
        if ord(ch) not in range(97,123) and ord(ch) not in range(65,91) and ord(ch) != 32 and ord(ch) != 45:
            return j2e(word)
        return e2j(word)

    
def lookupAll(wordList):
    if len(wordList)>1:
        df = DataFrame([lookupSingle(word) for word in wordList],columns=["Language","Word","Pronunciation","Meaning"])
    else:
        df = DataFrame([lookupSingle(wordList[0])],columns=["Language","Word","Pronunciation","Meaning"])
    return(df)