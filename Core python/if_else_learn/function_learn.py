# def my_function():
#   print("Hello from a function")
  
# my_function()

#Number of Arguments
# def person(fname, lname):
#     print(fname + " " + lname)
    
# person("Ambuj", "sharma")

#Arbitrary Arguments, *args
# def my_function(*kids):                  #Arbitrary Arguments
#     print("my kid name is : " + kids[2])

# my_function("ram", "shyam", "Lakshman","sheeta")

#Keyword Arguments
# def person (child1, child2, child3 ):
#     print("TYhe youngest child name is : " + child3)

# person(child1 = "xyz", child2 = "pqr", child3 = "lmn")

#Arbitrary Keyword Arguments, **kwargs
# def details(**kids):
#     print("My last name is : " + kids["lname"])
    
# details(fname = "Ambuj", lname = "Sharma")

# #Default Parameter Value
# def country_name(country = "india"):
#     print("my country name is : " + country)
    
# country_name("US")
# country_name("sweden")

#Passing a List as an Argument

# def my_function(food):
#     for x in food:
#         print(x)

# fruits = ["apple", "mango", "banana"]
# my_function(fruits)
    
#Return Values

def my_function(x):
    return 5 * x

print(my_function(10))