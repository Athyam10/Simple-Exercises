# Write a program that generates sum of 2 opearand equqlling to 10.
#  1 + 9 = 10
#  2 + 8 = 10
#  3 + 7 = 10
# ...
#  9 + 1 = 10

i = 1
j = 9;
while i<=9:
    print(f"{i} + {j} = {i+j}")
    i =i+1
    j=j-1