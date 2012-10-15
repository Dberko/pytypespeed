import time
import termios, fcntl, sys, os
import Tkinter as tk
b = True
i = 0
n = 0
a = True



def timer():
	global i
	global n
	global b
	n = 0
	while b == True:
		global i	
		time.sleep(1)
		i+= 1
		try:
            		c = sys.stdin.read(1)
			if c == "\n":
				print "Timer has stopped"
				a == False
				break
        	except IOError: pass
		print i
def getkey():
	fd = sys.stdin.fileno()

	oldterm = termios.tcgetattr(fd)
	newattr = termios.tcgetattr(fd)
	newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
	termios.tcsetattr(fd, termios.TCSANOW, newattr)

	oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
	fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

	try:
    		timer()
			

	finally:
    		termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)

	
getkey()
print "You're time was %d"% i




