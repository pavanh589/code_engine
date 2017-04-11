import time

class Networkerror(RuntimeError):
   def __init__(self, args):
      self.args = arg

def dec(n):
	print n
	print n == 700
	try:	
		if n == 700:
			raise Networkerror("not valid")
		
		if (n > 200 and n < 500):
			raise Exception("Not In a range", n)
				
		for i in range(0,n):
			time.sleep(2)
			print i
		return True	
	except KeyboardInterrupt:
		print "Keyboard Interreption"
		return False
	except Networkerror, e:
		print e
		return False
	except:
		print n
		print "Not in a Range"
	finally:
		print "close"
		
def add(array):
	summ = 0
	for i in array:
		summ = i + summ
	return summ
	
q = dec(700)			
print "result %s" %(q) 

s = add([1,2,3,4,5])
print s
