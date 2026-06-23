# Write a program that generates sum of 2 opearand equqlling to 10.
#  1 + 9 = 10
#  2 + 8 = 10
#  3 + 7 = 10
# ...
#  9 + 1 = 10

for i in range(1, 10):
    print(f"{i} + {10 - i} = 10")