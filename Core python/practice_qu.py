# sentence = input("Enter a sentence: ")
# unique_word = set(sentence.split())

# print("unique word:", unique_word)



# number = [1, 2, 2, 3, 2, 3, 4, 5]
# print(set(number))

# set1 = {1, 2, 3}
# # set2 = {4, 5, 6, 2, 3}
# # set3 = set1.intersection(set2)
# # print(set3)

# # set3 = set1.union(set2)
# # print(set3)

# # Define a set
# my_set = {"apple", "banana", "cherry", "orange"}

# # Get input from the user
# element = input("Enter an element to check: ")

# # Check membership and print result
# if element in my_set:
#     print("Yes")
# else:
#     print("No")


# number = {1, 2, 3, 4}

# check_element = input("Enter the element to check: ")

# if check_element in number:
#     print("yes")
# else:
#     print("No")


# person = {
#     "name": "Ambuj Sharma",
#     "age" : 50,
#     "city": "noida"
# }
# print(person)

# Count_Word_Frequency = input("write a sentence: ")


# Get input from the user
# sentence = input("Enter a sentence: ")

# # Split the sentence into words
# words = sentence.split()

# # Use a dictionary to count occurrences
# word_count = {}

# for word in words:
#     if word in word_count:
#         word_count[word] += 1  # Increase count if word exists
#     else:
#         word_count[word] = 1  # Initialize count if word is new

# # Print the result
# print("Word Frequency:", word_count)


# person = {
#     "name":"Ambuj Sharma",
#     "age":25,
#     "profession":"IT"
# }

# # person["age"]= 30
# # print(person["age"])

# person.update({"age": 30})
# # students.update({"city":"Noida"})

# print(person["age"])



# Dictionary of student marks
# student_marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 95,
#     "Eve": 88
# }

# # Initialize variables to track the highest score
# highest_score = -1
# top_student = ""

# # Loop through the dictionary to find the maximum value
# for student in student_marks:
#     if student_marks[student] > highest_score:
#         highest_score = student_marks[student]
#         top_student = student

# # Print the result
# print("Highest-scoring student:", top_student, "with marks", highest_score)


# # Dictionary of student marks
# student_marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 95,
#     "Eve": 88
# }

# # Find the student with the maximum marks
# #top_student = max(student_marks, key=student_marks.get)

# # Print the result
# #print("Highest-scoring student:", top_student, "with marks", student_marks[top_student])


# check_key = input("Enter key in dict: ")
# # check_value = input("enter value in dict: ")
# if check_key in student_marks:
#     print("yes")
# else:
#     print("No")

# print(student_marks.keys())

# Dictionary of student marks
# student_marks = {
#     "Alice": 85,
#     "Bob": 92,
#     "Charlie": 78,
#     "David": 95,
#     "Eve": 88
# }

# # Take user input to check if the key exists
# check_key = input("Enter a student's name: ")

# # Check if the key exists in the dictionary
# if check_key in student_marks:
#     print("Yes, the student exists in the dictionary.")
# else:
#     print("No, the student does not exist.")

# # Print all available keys (student names)
# print("Available students:", list(student_marks.keys()))


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# for x in thisdict.keys():
#   print(x)



# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}

# set3 = set1 - set2
# print(set3)


# set1.remove("apple")
# print(set1)

# set1.difference(set2)
# set1.add("lichi")

# set1.union(set2)


# # 🎓 Student Gradebook Dictionary
# student_marks = {
#     "Alice": [85, 90, 88],
#     "Bob": [75, 80, 72],
#     "Charlie": [95, 92, 98],
#     "David": [60, 70, 65],
#     "Eve": [88, 85, 90]
# }

# # 📊 Calculate and display each student's average marks
# print("📚 Student Gradebook (Average Marks):\n")

# for student, marks in student_marks.items():
#     # Calculate average marks for each student
#     average = sum(marks) / len(marks)
#     print(f"{student}: Marks = {marks} → Average = {average:.2f}")


# products = {
#     "laptop": 100,
#     "mobile": 50,
#     "mouse": 200
# }

# customer = input("enter the purchases value: ")

# for brand, quantity in products.items():
# #   print(brand, quantity)
  
#   final_laptop = quantity - int(customer)
#   print(f"{products}: total:{final_laptop}")
  
  
# 🛒 Inventory Management Dictionary
inventory = {
    "Apples": 20,
    "Bananas": 15,
    "Oranges": 10,
    "Mangoes": 5,
    "Grapes": 8
}

# 🔄 Display Current Inventory
def display_inventory():
    print("\n📦 Current Inventory:")
    for product, stock in inventory.items():
        print(f"{product}: {stock} units")
    print("-" * 30)

# 🛍️ Function to Purchase Product
def purchase_product(product, quantity):
    if product in inventory:
        if inventory[product] >= quantity:
            inventory[product] -= quantity
            print(f"\n✅ Successfully purchased {quantity} {product}.")
            
            # 🔔 Low Stock Alert
            if inventory[product] <= 5:
                print(f"⚠️ Warning: {product} stock is low! Only {inventory[product]} left.")
        else:
            print(f"\n❌ Not enough stock for {product}. Only {inventory[product]} available.")
    else:
        print(f"\n❌ {product} is not available in the inventory.")

# 📦 Display Initial Inventory
display_inventory()

# 🛒 Simulate Purchases
purchase_product("Apples", 5)
purchase_product("Mangoes", 3)
purchase_product("Oranges", 12)

# 📦 Display Updated Inventory
display_inventory()

  


        




