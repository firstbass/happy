#requires python2.7

#ywww
#!/usr/bin/env python
import os				#needed for multi-platform compatibility
import time				#needed to limit program speed
import thread			#needed for the magical "close on enter"

def input_thread(L):	#raw_input looks for enter in order to be like yooo that's my input
	raw_input()
	L.append(None)

def handle_it():
	question = raw_input('Would you like to use another string? (y|yes|Yes or n|no|No): ')
	while 1:	
		os.system('cls' if os.name == 'nt' else 'clear') 	
		if question == "y" or question == "yes" or question == "Yes":
			user_input()
		elif question == "n" or question == "no" or question == "No":
			print "Thanks for your time!"
			quit()
		else:
			question = raw_input("I didn't quite catch that." '\n' "Would you like to use another string? (y|yes|Yes or n|no|No): ")
def advance(b):			#what to do when current string is complete
	timeout = 0			#decides when _ blinks
	L = []				#magical array for closing program
	thread.start_new_thread(input_thread, (L,)) #start input thread

	while 1:			#loop for _
		os.system('cls' if os.name == 'nt' else 'clear') #clear
	 	timeout = timeout + 1	#counting variable
		if timeout % 2 == 0:	#if odd, print normal
			print b	
		if timeout % 2 != 0:	#if even, blink _
			print b + "_"	
		print '\n', "Press Enter to continue." #always ran
		time.sleep(0.5) 	#this is to give the blinking effect
		if L: 		
			os.system('cls' if os.name == 'nt' else 'clear') 
			handle_it() 	

def text_process(a):	#progressive text
	wordinprogress = ""	#empty variable needs to be initialized
	counter = 0			#counter variable
	storage = len(a)	#length of observed string			
	
	while counter < storage + 1:	#while counting variable is less than the full variable
		os.system('cls' if os.name == 'nt' else 'clear')	#clear screen
		counter = counter + 1		#counting
		if counter % 4 == 0 and counter != storage + 1:		#75% of the time, do not blink
			print wordinprogress							
		if counter % 4 != 0 and counter != storage + 1:		#25% of the time, blink _
			print wordinprogress + "_"
		if counter == storage + 1:	#prevents an overflow
			print a
			advance(b = a)	#hand off string to advance
		wordinprogress = a[:counter] #progressively grow the string in progress to hold the entire string
		time.sleep(0.07)	#slight pause
def user_input():
	c = raw_input('Please type the text you would like to see advance: ')
	text_process(a = c)
user_input()
