thisset = {"apple", "banana", "cherry"}
print(thisset)

my_set = {1, 2, 3, 4, 5, 6}
print(my_set)

# Using set() constructor
another_set = set([1, 2, 3, 4, 5, 6, 1, 2, 3, 3, 4, 4, 5])
print(another_set)

# Creating an empty set
empty_set = set()
print(type(empty_set))

#Add Elements (add())

my_set = {1, 2, 3}
my_set.add(6)
print(my_set)

#Remove Elements (remove() / discard() / pop())

my_set = {1, 2, 5, 6, 8, 3}
my_set.remove(3)          # Using remove() (raises an error if item not found)
print(my_set)

my_set = {1, 2, 5, 6, 8, 3}
my_set.discard(10)        # Using discard() (does NOT raise an error if item not found)
print(my_set)

#Check Membership (in)

my_set = {1, 2, 3, 5}
print(2 in my_set)
print(10 in my_set)

#Set Union (| or union())

set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
print(union_set)      #Combines two sets (removes duplicates).

union_set = set1.union(set2)
print(union_set)

#Set Intersection (& or intersection())

set1 = {1, 2, 3}
set2 = {3, 4, 5}

ingtersection_set = set1 & set2
print(ingtersection_set)

ingtersection_set = set1.intersection(set2)
print(ingtersection_set)

#Set Difference (- or difference())

set1 = {1, 2, 3, 4, 9}
set2 = {3, 4, 5, 6}

diff_set = set1 - set2
print(diff_set)

diff_set =set1.difference(set2)
print(diff_set)

#Symmetric Difference (^ or symmetric_difference())
set1 = {1, 2, 3, 4, 9}
set2 = {3, 4, 5, 6}

sym_diff_set = set1 ^ set2
print(sym_diff_set)

sym_diff_set = set1.symmetric_difference(set2)
print(sym_diff_set)

#Subset & Superset

set1 = {1, 2}
set2 = {1, 2, 3, 4}

# Subset (set1 is a subset of set2)
print(set1.issubset(set2))

# Superset (set2 is a superset of set1)
print(set2.issuperset(set1))

#⚡ Other Useful Set Methods

my_set = {1, 2, 3}
# Copy a set
new_set = my_set.copy()
print(new_set)

# Clear all elements
# new_set = my_set.clear()
# print(new_set)

# Length of set
print(len(new_set))



#🚀 Example Use Case: Remove Duplicates from List

numbers  = [1, 2, 3, 4, 5, 6, 1, 2, 3, 3, 4, 4, 5, 10, 10]
unique_number = list(set(numbers))
print(unique_number)


#To add multiple items from more_fruits to the fruits set, use the update() method.
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

# Add multiple items to the set
fruits.update(more_fruits)

print(fruits)

#Explanation:
#Sets in Python are unordered collections, meaning the items are stored in a way that doesn't maintain the order of insertion. 
# When you loop through a set, the order of items will appear random and can change each time you run the code.
#True or False. Sets are unordered, so when you loop through the items, the order will be totally random.
#true

fruits = {"apple", "banana", "cherry", "orange", "mango"}

# Loop through the set
for fruit in fruits:
    print(fruit)
    
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# Find common items (duplicates)
common = set1.intersection(set2)
print(common)

common = set1 & set2
print(common)


# List of subjects
subjects = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]

# Use a set to find unique subjects
unique_subjects = set(subjects)

# Count of unique subjects = number of classrooms required
classrooms_needed = len(unique_subjects)

# Display the result
print(f"Unique subjects: {unique_subjects}")
print(f"Total classrooms needed: {classrooms_needed}")

#Store as Strings
#In Python, 9 and 9.0 are considered equal because Python treats integers and floating-point numbers as equivalent when comparing values. 
#This happens because of Python's internal type conversion.
#However, you can store them separately in a set by converting them into different data types, such as:

#✅ Solution 1
unique_set = {9, "9.0"}
print(unique_set)

#✅ Solution 2
unique_set = {
    (int, 9), 
    (float, 9.0)
    }
print(unique_set)

#✅ Solution 3
unique_set = {9, 9.0 + 0j}
print(unique_set)
