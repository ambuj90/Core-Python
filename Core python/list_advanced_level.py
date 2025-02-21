#List Comprehension (Compact & Fast Way to Create Lists)

# Create a list of squares of numbers from 1 to 5
squares = [x**2 for x in range(1,6)]
print(squares)

# Get only even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens =[x for x in numbers if x % 2 == 0]
print(evens)

# Convert all strings in a list to uppercase

fruits = ["apple", "banana", "cherry"]
upper_fruits = [fruit.upper() for fruit in fruits]   #fruit.upper() converts each string to uppercase.
print(upper_fruits)

# upper_fruits = [fruit.upper() for fruit in fruits]

# upper_fruits = []
# for fruit in fruits:
#     upper_fruits.append(fruit.upper())

#Using map() and filter() with Lists

# Double each number using map()
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Filter even numbers using filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

odd =list(filter(lambda x: x % 3 == 0, numbers))
print(odd)


#Using enumerate() with Lists
fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(index, fruit)


#Using set() to Remove Duplicates in a List

numbers_list = [1, 2, 3, 4, 5, 6 ,9 ,8, 15, 3, 2, 1, 5, 15, 6, 2, 9]
unique_numbers = list(set(numbers_list))
print(unique_numbers)

# fruits = ["apple", "banana", "cherry"]
# print(fruits[2])


mylist = ['apple', 'banana', 'cherry']
mylist[1:2] = ['kiwi', 'mango']
print(mylist[2])

fruits = ['apple', 'banana', 'cherry']
tropical = ['mango', 'pineapple', 'papaya']
fruits.extend(tropical)  # Adds elements of tropical to fruits
print(fruits)


