# #Dictionary
# #Dictionaries are used to store data values in key:value pairs.

# #A dictionary is a collection which is ordered*, changeable and do not allow duplicates.


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(thisdict)

# person = {
#     "name" :"Ambuj",
#     "age"  : 32,
#     "subject": "python"
# }
# print(person)
# print(person["age"])

# #Duplicate values will overwrite existing values:
# person = {
#     "name" :"Ambuj",
#     "age"  : 32,
#     "subject": "python",
#     "age": 40
# }
# print(person)
# print(len(person))

# #The values in dictionary items can be of any data type:
# person = {
#     "name" :"Ambuj",
#     "age"  : 32,
#     "subject": "python",
#     "age": 40,
#     "colors":[
#         "red",
#         "white",
#         "green"
#     ]
# }
# print(person)
# print(type(person))

# #It is also possible to use the dict() constructor to make a dictionary.
# person = dict(name = "John", age = 36, country = "Norway")
# print(person)


# student = {
#     "name": "Alice",
#     "age": 22,
#     "major": "Computer Science"
# }
# print(student)

# employee = dict(name="John", age=30, department="HR")
# print(employee)

# #✅ Method 3: From Lists of Tuples

# pairs = [("name", "Emma"), ("age", 25), ("city", "Paris")]
# info = dict(pairs)
# print(info)

# #✅ Method 4: Using Dictionary Comprehension

# squares = {x: x**2 for x in range(1, 6)}
# print(squares)


# #✅ Access Using Key ([] and get())

# person = {"name": "John", "age": 30, "city": "New York"}

# # Using square brackets
# print(person["name"])  # Output: John

# # Using get() method
# print(person.get("age"))  # Output: 30

# # Using get() with default value
# print(person.get("country", "USA"))  # Output: USA

# # ✅ Add New Key-Value Pair

# person["job"] = "engineer"
# print(person)

# # ✅ Update Existing Key
# person["age"] = 35
# print(person)

# # ✅ Using update() Method

# person.update({"city": "Los Angeles" ,"country": "india"})
# print(person)

# # ✅ Loop Through Keys

# person = {"name": "John", "age": 30, "city": "New York"}
# for key in person:
#     print(key, ":", person[key])
    
# # ✅ Loop Through Values

# for value in person.values():
#     print(person)
    
    
# #✅ Loop Through Key-Value Pairs

# for key, value in person.items():
#     print(f"{key}: {value}")      # f"" is a formatted string literal (f-string). It allows you to embed variables directly inside a string.


# #🚀 Real-World Example: Count Word Frequency    
# text = "apple banana apple orange banana apple"
# words = text.split()

# word_count = {}
# for word in words:
#     word_count[word] = word_count.get(word, 0) + 1

# # Display word frequencies
# for word, count in word_count.items():
#     print(f"{word}: {count}")

# # 🌟 8. Advanced Dictionary Operations
# #1️⃣ Dictionary Comprehension
# # Example: Square of numbers
# squares = {x: x**2 for x in range(1, 6)}
# print(squares)

# #2️⃣ Nested Dictionaries
# students = {
#     "student1": {"name": "Alice", "age": 22},
#     "student2": {"name": "Bob", "age": 23}
# }
# print(students["student1"]["name"])  # Output: Alice

# #3️⃣ Merging Dictionaries

# dict1 = {"a":1, "b": 3, "c": 9}
# dict2 = {"b":5, "c": 5}

# dict3 = dict1 | dict2
# print(dict3)

# #4️⃣ Sorting Dictionary by Keys or Values
# sorted_by_keys = dict(sorted(person.items()))
# print(sorted_by_keys)


# # Sort by values
# person = {
#     "name": "John",   # String
#     "age": 30,        # Integer
#     "city": "New York"  # String
# }

# # Sorting by values
# sorted_by_values = dict(sorted(person.items(), key=lambda item: str(item[1])))
# print(sorted_by_values)

# #explain code
# #👉 Step 1: person.items()

# #person.items() returns all key-value pairs as tuples.
# #Output of person.items():
# #dict_items([('name', 'John'), ('age', 30), ('city', 'New York')])

# #👉 Step 2: sorted(..., key=lambda item: str(item[1]))

# # The sorted() function sorts the items based on the key argument.
# # lambda item: str(item[1]) means:
# # item represents each (key, value) tuple.
# # item[1] refers to the value (second element of the tuple).
# # str(item[1]) converts each value to a string before sorting.
# # Sorting Process:

# # Values become:
# # "John", "30", "New York"
# # When sorted as strings:
# # "30", "John", "New York"

# # 👉 Step 3: dict(...)

# # sorted(...) returns a list of tuples:
# #     [('age', 30), ('name', 'John'), ('city', 'New York')]

# # dict(...) converts this sorted list back into a dictionary.
# # print(sorted_by_values)
# # {'age': 30, 'name': 'John', 'city': 'New York'}

# # person.items() gives key-value pairs as tuples.
# # sorted(..., key=lambda item: str(item[1])) sorts based on values converted to strings.
# # dict(...) converts the sorted list back into a dictionary.

# students = {
#     "name": ["Ambuj Sharma", "rohit", "sagar"],
#     "student1": {"name": "Alice", "age": 22},
#     "student2": {"name": "Bob", "age": 23},
#     "subject" : {
#         "phy" : 89,
#         "chem": 90,
#         "math": 99
#     }
    
# }
# print(students.keys())
# print(list(students.keys()))
# print(len(students))
# print(len(students.keys()))
# print(students.values())
# print(list(students.values()))

# print(students.items())

# pairs = list(students.items())
# print(pairs[0])

# print(students["name"])
# #get

# print(students["name"])
# print(students.get("name"))

# # print(students["name2"])  # return error
# print(students.get("name2"))  # No error => None

# students.update({"city":"Noida"})
# print(students)

# new_dict = {"city": "delhi", "age": 20}
# students.update(new_dict)
# print(students)

# #Python program to enter marks of 3 subjects from the user and store them in a dictionary, where the subject name is the key and the marks are 
# # the value.

# # Initialize an empty dictionary to store subject marks
# marks_dict = {}

# # Input marks for 3 subjects from the user
# for i in range(3):
#     subject = input(f"Enter the name of subject {i+1}: ")
#     marks = int(input(f"Enter marks for {subject}: "))
    
#     # Add subject and marks to the dictionary
#     marks_dict[subject] = marks

# # Display the final dictionary
# print("\n📚 Subject Marks Dictionary:")
# print(marks_dict)



# marks = {}

# x = int(input("enter phy: "))
# marks.update({"phy": x })

# x = int(input("enter math: "))
# marks.update({"math": x })

# x = int(input("enter chem: "))
# marks.update({"chem": x })

# print(marks)


car = {
    "brand" : "Ford",
    "price" : 300,
    "quantity": 20,
    "year": 1964
}

# x = car.get("price")
# print(x)

# y = car.keys()
# print(y)

# car["color"] = ["white"]
# # print(car)
# car["year"] = 1984

# z = car.values()
# print(z)

# z =car.items()
# print(z)

# car["year"] = 2020
# print(car)

# car.update({"year" : 2025, "color": "red"})
# print(car)

# # 🎨 Dictionary Comprehension to generate squares
# squares = {num: num**2 for num in range(1, 6)}

# # 📊 Display the dictionary
# print("🔢 Dictionary of Squares:")
# for key, value in squares.items():
#     print(f"{key} → {value}")



# cube = {num : num**3 for num in range(1,8)}

# print("dict of cubes:")
# for key, value in cube.items():
#     print(f"{key} : {value}")   
    
    
    
# from collections import defaultdict

# # 📋 List of dictionaries (Example: Employees with departments)
# employees = [
#     {"name": "Alice", "department": "HR"},
#     {"name": "Bob", "department": "IT"},
#     {"name": "Charlie", "department": "HR"},
#     {"name": "David", "department": "Finance"},
#     {"name": "Eve", "department": "IT"},
#     {"name": "Frank", "department": "Finance"},
#     {"name": "Grace", "department": "HR"}
# ]

# # 🔄 Group by 'department'
# grouped_by_department = defaultdict(list)

# for emp in employees:
#     department = emp["department"]
#     grouped_by_department[department].append(emp["name"])

# # 📊 Display grouped results
# print("\n🟢 Employees Grouped by Department:")
# for department, names in grouped_by_department.items():
#     print(f"\n📂 {department}:")
#     for name in names:
#         print(f"  - {name}")


# 📋 List of employee dictionaries
# employees = [
#     {"name": "Alice", "department": "HR"},
#     {"name": "Bob", "department": "IT"},
#     {"name": "Charlie", "department": "HR"},
#     {"name": "David", "department": "Finance"},
#     {"name": "Eve", "department": "IT"},
#     {"name": "Frank", "department": "Finance"},
#     {"name": "Grace", "department": "HR"}
# ]

# # 🔄 Step 1: Create an empty dictionary to group by department
# grouped = {}

# # 🔍 Step 2: Group employees by department
# for emp in employees:
#     dept = emp["department"]  # Get the department
#     name = emp["name"]        # Get the employee name

#     if dept not in grouped:
#         grouped[dept] = []    # Create a new list if department doesn't exist

#     grouped[dept].append(name)  # Add employee name to the department list

# # 📊 Step 3: Display results
# print("\n🟢 Employees Grouped by Department:")
# for dept, names in grouped.items():
#     print(f"\n📂 {dept}:")
#     for name in names:
#         print(f"  - {name}")



# 📚 Step 1: Nested dictionary of student details
# students = {
#     "Student1": {
#         "name": "Alice",
#         "age": 20,
#         "subjects": {
#             "Math": 85,
#             "Science": 90,
#             "English": 88
#         }
#     },
#     "Student2": {
#         "name": "Bob",
#         "age": 21,
#         "subjects": {
#             "Math": 78,
#             "Science": 85,
#             "English": 80
#         }
#     },
#     "Student3": {
#         "name": "Charlie",
#         "age": 19,
#         "subjects": {
#             "Math": 92,
#             "Science": 88,
#             "English": 84
#         }
#     }
# }

# # 🔍 Step 2: Display student details
# print("\n🎓 Student Details:")
# for student_id, details in students.items():
#     print(f"\n📄 {student_id}:")
#     print(f"  Name: {details['name']}")
#     print(f"  Age: {details['age']}")
#     print("  Subjects and Marks:")
#     for subject, marks in details['subjects'].items():
#         print(f"    {subject}: {marks}")



# number= [1,2,3]
# print(number[ : ])



# x = {'type' : 'fruit', 'name' : 'banana'}

# x['type'] ="berry"
# print(x)


# a = {
#     'name' : 'John', 
#     'age' : '20'
#     }
# b = {
#     'name' : 'May', 
#     'age' : '23'
#     }
# customers = {
#     'c1' : a, 
#     'c2' : b
#     }

# print(customers['c2']['name'])

a = {'name' : 'John', 'age' : 20}
b = {'name' : 'May', 'age' : 23}
customers = {'c1' : a, 'c2' : b}
for x, obj in customers.items():
  print(x)
    
  for y in obj:
    print(y + ':', obj[y])