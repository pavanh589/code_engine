import time

def dec(n):
	try:
		for i in range(0,n):
			time.sleep(2)
			print i
		return True	
	except KeyboardInterrupt:
		print "Keyboard Interreption"
		return False
	finally:
		print "close"
		print "finally"

q = dec(100)			
print "result %s" %(q) 
