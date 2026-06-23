import myPythonLibrary as myLib

# The usage of the funtion, or Function call
str1 = myLib.getAStringFromUser()
print("This is what you entered: ==> ", str1)

# count number of occurrences of each digit, 0 - 9
numOccurences = myLib.countNumOccurrences4Digits(str1)
print(numOccurences)

# Now let us draw the histogram
myLib.drawHistogram(numOccurences)




