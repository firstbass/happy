#! /usr/bin/env python
#Invoke this script as, well, a script. 'python hap.py' should do the trick.
#Python string script
#textboxstring.py
#V0.2 - Getting the terminal down!
import os
import time
import thread
def input_thread(L):
    raw_input()
    L.append("yo")
def handle(a):
    os.system('clear')
    print a + '\n'
    question = raw_input("Would you like to do it again? y/n ")
    while 1:    
        os.system('clear')
        print a + '\n'        
        if question == "y":
            user_input()
        elif question == "n":
            os.system('clear')
            quit()
        else:        
            question = raw_input("Sorry, I didn't quite catch that." '\n' "Would you like to do it again? y/n ")
def do_print(b):
    L = []
    counter = 1
    thread.start_new_thread(input_thread, (L,))
    while 1:
        os.system('clear')
	counter = counter + 1
        if counter % 2 == 0:
            print b + "_"
        elif counter % 2 != 0:
            print b
        if L:  
            handle(a = b)
        print '\n' + "Press Enter to continue."
        time.sleep(.1)
def tprocess(c):
    counter = 0   
    storage = len(c)
    wordinprogress = ""
    while counter < storage + 1:
        os.system('clear')
        counter = counter + 1    
        if counter % 4 != 0 and counter != storage + 1:
            os.system('clear')
            print wordinprogress
        if counter % 4 == 0 and counter != storage + 1:
            os.system('clear')
            print wordinprogress + "_"
        if counter == storage + 1:
            do_print(b = c)
        wordinprogress = c[:counter]
        time.sleep(0.07)
def user_input():
    os.system('clear')
    string = raw_input("Please type desired text: ")
    tprocess(c = string)
user_input()