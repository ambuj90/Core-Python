tup =(10, 2, 5, 8)
print(tup[0])
print(tup[1])
print(tup[2])

# tup[0] = 5

# tup =(1,)
# print(type(tup))

tup1 = (2, 1, 2, 3, 1, 2, 15, 2)
print(tup1.index(15))
print(tup1.count(2))


movies = []
# mov1  = input("Enter 1st Movie: ")
# mov2  = input("Enter 2nd Movie: ")
# mov3  = input("Enter 3rd Movie: ")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

#or

movies.append(input("enter your 1st movie: "))
movies.append(input("enter your 2nd movie: "))
movies.append(input("enter your 3rd movies"))
print(movies)


# txt = 'The best things in life are free!'
# if 'free' in txt:  # Use 'in' to check if 'free' exists in txt
#   print('Yes, free is present in the text.')


# thistuple = ("apple", "banana", "cherry")
# for i in range(len(thistuple)):  # Use range() to iterate over index numbers
#     print(thistuple[i])  # Access elements using index
    
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])

# Negative Indexing:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])

# -1 → "mango"
# -2 → "melon"
# -3 → "kiwi"
# -4 → "orange"
# -5 → "cherry"
# -6 → "banana"
# -7 → "apple"
# Slice [-4:-1] means:

# Start from index -4 → "orange"
# Go up to index -1 (excluded) → "mango" is not included.
# output is: ("orange", "kiwi", "melon")

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")
  
name = ("ambuj", "rohit", "sagar")
if "sagar" in name:
    print("yes", 'sagar in the tupple list')


x = ("apple", "banana", "cherry")
y = list(x)         # y= ["apple", "banana", "cherry"]
y[1] = "kiwi"       # y= ["apple", "kiwi", "cherry"]
x = tuple(y)        # x= ("apple", "kiwi", "cherry")

print(x)           #('apple', 'kiwi', 'cherry')


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple)


thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


# thistuple = ("apple", "banana", "cherry")
# del thistuple
# print(thistuple)    #this will raise an error because the tuple no longer exists


fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)