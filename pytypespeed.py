import time
import termios, fcntl, sys, os
counting = True
counter = 0


def timer():
	global counter
	global counting
	n = 0
	while counting == True:
		global counter	
		time.sleep(1)
		counter+= 1
		#Tries to see if RETURN was pressed
		try:
            		c = sys.stdin.read(1)
			# \n means that user has hit RETURN
			if c == "\n":
				print "Timer has stopped"
				break
        	except IOError: pass
		print counter


def getkey():		#Checks for keypress in background
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
print "You're time was %d"% counter




