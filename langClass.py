#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 01:22:04 2023

@author: peterlai
"""

import pandas as pd
from common import wordChangeForm
import hangman


class Word:
    def __init__(self,filename):
        if not ".csv" in filename: 
            filename += ".csv"
        try:
            df = pd.read_csv(filename)
        except FileNotFoundError:
            self.word = "apple"
            self.pron = "ˈæpl"
            self.meaning = "リンゴ"
        else:
            sample = df.sample()
            self.word = sample.iloc[0][0]
            self.pron = sample.iloc[0][1]
            self.meaning = sample.iloc[0][2]
        self.gamePass = True
    def typingQuiz(self,attempt=5):
        question = self.meaning.replace(self.word,"___")
        print("Meaning:",question)
        answer = wordChangeForm(self.word)
        print(f"({attempt} attempt(s) left.)") 
        while (attempt>0):            
            entering = wordChangeForm(input("Enter the word: "))
            if entering == answer or entering == self.pron:
                print("You win!")
                break
            else:
                print("Wrong Answer!")
                attempt -= 1
                print(f"({attempt} attempt(s) left.)") 
        else:
            print("You lost!")
            self.gamePass = False
        print(f"Correct Answer: {self.word}")
            
            
class English(Word):
    def hangmanGame(self):
        alphaList = [chr(i) for i in range (97,123)]
        answer = wordChangeForm(self.word)
        questionList = []
        for ch in answer:
            if ch.isalpha():
                questionList.append("*")
            else:
                questionList.append(ch)
        time = 0
        while(True):
            questionStr = "".join(questionList)
            print(f"Question: {questionStr}")
            print(f"Available Alphabet:{' '.join(alphaList)}")
            while(True):
                print("Please enter only an alphabet you haven't entered to guess.")
                entering = input().lower()
                if entering in alphaList:
                    break
            alphaList.remove(entering)
            if entering in answer:
                print("Nice Guess!")
                for j in range(len(answer)):
                    if entering == answer[j]:
                        questionList[j] = entering
                if not "*" in questionList:
                    print("You win! You have rescued the guy!")
                    break
            else:
                print("Wrong Guess!")
                print(hangman.hangmanPic[time])
                time += 1
                if time == 9:
                    print(f"HINT: {self.meaning}")
                if time == 10:
                    self.gamePass = False
                    break
        print(f"Correct Answer: {self.word}")
        
class Japanese(Word):
    def pronTest(self,attempt=5):
        question = self.word
        print("Word:",question)
        answer = self.pron
        print(f"({attempt} attempt(s) left.)") 
        while (attempt>0):            
            entering = wordChangeForm(input("Enter the pronunciation in Hiragana: "))
            if entering == answer:
                print("You win!")
                break
            else:
                print("Wrong Answer!")
                attempt -= 1
                print(f"({attempt} attempt(s) left.)") 
        else:
            print("You lost!")
            self.gamePass = False
        print(f"Correct Answer: {answer}")