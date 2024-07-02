#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 01:27:34 2023

@author: peterlai
"""
import datetime as dt
import process as ps

start = dt.datetime.now()

print("""
-----------------------------------------      
Peter Lai's Language Learning Program
-----------------------------------------
""")

while(True):
    try:
        cmd = int(input("""
What do you want to do now?
1. Input new words into a .txt file.
2. Look up the dictionary for an existing .txt file of words and save the file as .csv
3. Have a typing quiz (Available for English and Japanese words)
4. Have a hangman game (Available for English words only)
5. Have a pronunciation test (Available for Japanese words only)
6. End the program
"""))
    except ValueError:
        cmd = 0
    else:
        if cmd ==1:
            ps.startInputNew()
        elif cmd ==2:
            ps.startLookup()
        elif cmd ==3:
            ps.startTypingQuiz()
        elif cmd ==4:
            ps.startHangmanGame()
        elif cmd ==5:
            ps.startPronTest()
        elif cmd ==6:
            ps.endProgram()
            break

end = dt.datetime.now() 
print(f"Time of Use: {end - start}")        