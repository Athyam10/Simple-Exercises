import threading

def function1():
	for x in range(1,500):
		print("Hello Hasan")

		
def function2():
	for x in range(1,500):
		print("Hi All")

		
		
""" 
function1()
function2()
""" 

t1 = threading.Thread(target=function1)
t2 = threading.Thread(target=function2)
t1.start() # We need to use start() function instead of run() function, which executes in sequential instead of parallel
t2.start()

