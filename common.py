#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 01:23:51 2023

@author: peterlai
"""
from math import ceil

def wordChangeForm(word):
    newWord=""
    for c in word:
        if 12449<ord(c)<12535:
            c = chr(ord(c)-96)
        newWord += c
    newWord = newWord.lower()
    return(newWord)

def showRecord(playtime,record):
    passtime = list(record.values()).count(True)
    print(f"Among {playtime} times you played, you passed {passtime} times.",end=" ")
    print(f"(Passing Rate:{ceil((passtime/playtime)*100)}%)")