# Defition of the function
def getAStringFromUser():
	aSentence = input("Please Enter a sentence with digits in it")
	return aSentence

def countNumOccurrences4Digits(myStr):
	digits = [0]*10 # an array of size 10, with 0 value
	for x in myStr:
		if x.isdigit():
			digits[int(x)] +=1
	return	digits

# A function that draws histogram of entries of a given array
def drawHistogram(numbs):
	for i in range(len(numbs)):
		print(i,":", '*'*numbs[i])
