import threading

def helloWorld():
	for x in range(25):
		print("Hello Hasan")

""" 
t1 = threading.Thread(target=helloWorld)
t1.start()
print("When this is goint to be printed?") # Even though this is the last part of the code, could it be printed before helloWorld?
""" 

# what happens with this code?
t1 = threading.Thread(target=helloWorld)
t1.start()
t1.join() # Do not go to the next statement until my thread t1 is done
print("When this is goint to be gprinted?") # Even though this is the last part of the code, could it be printed before helloWorld?
