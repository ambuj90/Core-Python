mylist = ["apple", "banana", "cherry"]
print (mylist)
list1 = ["apple", "banana", "xyz","pqr" ,"cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
print(list1)
print(list2)
print(list3)
print(type(mylist))
print(list1[1])
list1.sort()
print(list1)
list1.pop()
print(list1)

print(list1)

# Creating a mixed list
my_list = ["dog", 3, True, 4.5, ["apple", "banana"]]
print(my_list[0])  # Output: 'dog'
print(my_list[1])  # Output: 3
print(my_list[4])  # Output: ['apple', 'banana']
print(my_list[4][1])

# Adding an element to the list
my_list.append("new_item")
print(my_list)

# Inserting an element at a specific position

my_list.insert(1,"cat")
print(my_list)

# Removing an element
my_list.remove(3)

print(my_list)

# Checking length of the list
print(len(my_list))

# Extending the list with another list
extra_items = ["grapes", "orange"]
my_list.extend(extra_items)
print(my_list)



#===========================================================================================

# Original list
original_list = ["apple", "banana", "cherry"]
copied_list =original_list.copy()
copied_list.append("orange")
print(original_list)
print(copied_list)

#✅ Observation: The original list remains unchanged even after modifying the copied list.


my_list = ["apple", "banana", "cherry"]  # List of strings
num_list = [1, 2, 3, 4, 5]  # List of integers
mixed_list = ["hello", 42, True, 3.14]  # List with different data types

print(my_list)  # Output: ['apple', 'banana', 'cherry']
print(num_list)  # Output: [1, 2, 3, 4, 5]
print(mixed_list)  # Output: ['hello', 42, True, 3.14]


fruits = ["apple", "banana", "cherry"]
fruits.insert(2, "lemon")
print(fruits)


mylist = ['apple', 'banana', 'cherry']  # Create a list
mylist[0] = 'kiwi'  # Replace 'apple' (index 0) with 'kiwi'
print(mylist[1])  # Print the second item (index 1)