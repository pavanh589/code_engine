import time

class Networkerror():
   def __init__(self, args):
      self.args = args

class Simpleerror(RuntimeError):
   def __init__(self, args):
      self.args = args
      
def dec(n):
	try:	
		if n == 700:
			raise Networkerror(n)
		
		if n == 100:
			raise Simpleerror("Invalid")
				
		for i in range(0,n):
			time.sleep(2)
			print i
		return True	
	except Networkerror, e:
		print e.args
		return False
	except Simpleerror, e:
		print e	
	finally:
		print "close"
		
def add(array):
	summ = 0
	for i in array:
		summ = i + summ
	return summ
	
q = dec(100)			
print "result %s" %(q) 

s = add([1,2,3,4,5])
print s
