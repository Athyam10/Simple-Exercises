# TUPLES ===>  ordered, IMMUTABLE, allows duplicates
mytuple = ("Max", 28, "Boston")

print(mytuple)

print("Printing the indivudual elements")
print(mytuple[0])
print(mytuple[-1])

# item = mytuple[4]  # Index out of range error

#mytuple[0] = "Tim"  # IS NOT allowed, as tuple is IMMUTABLE


for z in mytuple:
    print(z)

if "Tim" in mytuple:
    print("Yes it is in")
else:
    print("No it is not")

# Let us play with tuples
my_tuple = ('a', 'p', 'p', 'l', 'e')

# length of a tuple
print(len(my_tuple))

# counting elements in tuple
print(my_tuple.count('p'))
print(my_tuple.count('0'))
print(my_tuple.count('k')) # not in the tuple
#print(my_tuple.index('o')) # finding 1st index of the element



# can covert tuple to LIST or viceversa
my_list = list(my_tuple)
print(my_list)


my_tuple2 = tuple(my_list)
print(my_tuple2)

# Slicing with tuples
a = (1, 2, 31, 4, 0, 25, 6, -7, 8, 9, 10)
b=a[2:5]
print(b)  # last index 5, is not included



b = a[:5]    # goes from 1st index to 5th
b = a[2:]    # goes from the 2nd index all the way to the last
b = a[::2]   # in steps 2, from beginning to the end (default is a[::1]
b = a[::-1]  # to reverse
print(a)
print(b)


# unpacking
my_tuple = "Max", 28, "Boston"
name, age, city = my_tuple
print(name)
print(age)
print(city)

# unpacking multiple elements
my_tuple = (0,1,2,3,4)
i1,*i2, i3 = my_tuple
print(i1)
print(i3)
print(i2)