#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 15:53:19 2023

@author: peterlai
"""

import wordProcess as wp
import lookup as lu
from langClass import Word,English,Japanese
from common import showRecord


def wordChangeForm(word):
    newWord=""
    for c in word:
        if 12449<ord(c)<12535:
            c = chr(ord(c)-96)
        newWord += c
    newWord = newWord.lower()
    return(newWord)


def startInputNew():
    filename = input("Please decide the name of the .txt file:")
    wp.writeRawWord(filename)
    print("File saved.")


def startLookup():
    filename = input("Please enter the name of the .txt file:")
    e2jName = input("Please decide the name of the .csv file that stores English words:")
    j2eName = input("Please decide the name of the .csv file that stores Japanese words:")
    wp.writeNote(lu.lookupAll(wp.readRawWord(filename)),e2jName,j2eName)
    print("File saved.")

    
def startTypingQuiz():
    filename = input("Please enter the name of the .csv file that stores words:")
    while(True):
        try:
            playtime = int(input("How many times do you want to play?"))
        except ValueError or playtime<1:
            print("Please enter an integer number larger than 0!")
        else:
            break
    record = {}
    for i in range(playtime):  
        print("===============")
        print(f"Round {i+1}")
        print("===============")
        w = Word(filename)
        w.typingQuiz()
        record.update({i+1:w.gamePass})
    showRecord(playtime,record)
    
    
def startHangmanGame():
    filename = input("Please enter the name of the .csv file that stores English words:")
    while(True):
        try:
            playtime = int(input("How many times do you want to play?"))
        except ValueError or playtime<1:
            print("Please enter an integer number larger than 0!")
        else:
            break
    record = {}
    for i in range(playtime):  
        print("===============")
        print(f"Round {i+1}")
        print("===============")
        e = English(filename)
        e.hangmanGame()
        record.update({i+1:e.gamePass})       
    showRecord(playtime,record)

    
def startPronTest():
    filename = input("Please enter the name of the .csv file that stores Japanese words:")
    while(True):
        try:
            playtime = int(input("How many times do you want to play?"))
        except ValueError or playtime<1:
            print("Please enter an integer number larger than 0!")
        else:
            break
    record = {}
    for i in range(playtime):  
        print("===============")
        print(f"Round {i+1}")
        print("===============")
        j = Japanese(filename)
        j.pronTest()
        record.update({i+1:j.gamePass})
    showRecord(playtime,record)


def endProgram():
    print("Thanks for your use. Hope you enjoy the learning!")
