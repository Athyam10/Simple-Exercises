# Write a program that take a number from a user and outputs 
# on sentence only as;
# X is positive Odd or Even
# X is negative Odd or Even
# X is Zero, where x is the number user enters

# Ask user enter a number and convert it to an integer
number = int(input("Please enter a number"))
print("You have entered this number: ", number)

# Determine whether the number is positive or negative or zero
if number > 0:
	#determine whether the number is odd or even
	if number%2 == 0: # number must be even
		print(number, " is postive and even")
	else:
		print(number, " is positive and odd")
elif number < 0:
	#determine whether the number is odd or even
	if number%2 == 0: # number must be even
		print(number, " is negative and even")
	else:
		print(number, " is negative and odd")
else:
	print(number, " is ZERO")
