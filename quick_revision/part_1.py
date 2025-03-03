# user = input("Enter user Name: ")
# pwd = input('Enter Pwd: ')
# if user == "Ambuj" and pwd == "Python":
#     print("Enter the correct username and pwd")
# else:
#     print("Wrong input values") 
    
# in and not in    


# print(10,20,30,40,50, sep = "-")

# print(10 , end = " ")
# print(20 , end = " ")
# print(30, end = " ")

# print(10, 20, 30, sep = ":" , end = ":")
# print("A", "B", "C", sep = ":", end = "")


# name = "Ambuj"
# marks = 100
# salary = 100000000
# print('Name: {}, marks: {}, salary: {}'. format(name, marks, salary))


# l = [0, 5 ,10, 15, 20, 25, 30]

# for x in l:
#     if x % 2 == 0:
#         continue
#     print(x)
    
# x = [10,20,30]      
# del x
# print(x)

# x = [10,20,30] 
# l = []

# l.append(x)
# l[0].remove(x[0])
# print(l)


# x = [10,20,30] 
# l = []

# l.extend(x)
# print(l)

# l.remove(x[1])
# print(l)



# List compresion

# l = [x for x in range(1,11) if x % 2 == 0 ]
# print(l)



# s = set()

# s.add(10)
# s.add(20)
# s.add(30)

# print(s)
# s.remove(10)
# print(s)


# dictionary:

# d = {}

# d[key] = value

# del d[key]

# d.get(key)

# Function:


# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")


# x = lambda n : n*n
# print(x(4))


# Dcorator and Generators
# def my_decorator(func):
#     def wrapper():
#         print("🔥 Before the function runs")
#         func()
#         print("✅ After the function runs")
#     return wrapper

# @my_decorator  # Using the decorator
# def say_hello():
#     print("Hello, World!")

# say_hello()


# Decorator with Arguments

# def repeat(n):
#     def decorator(func):
#         def wrapper():
#             for _ in range(n):
#                 func()
#         return wrapper
#     return decorator

# @repeat(3)  # Calls function 3 times
# def greet():
#     print("Hello!")

# greet()







# Modules

# A group of functions, Variables, classes saved to a file is called a module.

# import ambujdjango

# ambujdjango.connect()
# ambujdjango.display('Hello Good Morning')
# ambujdjango.disconnect()

# from ambujdjango import*
# from django.http import HttpResponse
# connect()
# display('Hello Good Morning!!!')
# disconnect()


# from ambujdjango import connect as c, display as d, disconnect as dc
# c()
# d("Hello! Good morning!!")
# dc()


#Packege:

# A group of related modules into a single unit is called as Package.

# __init__() =====>>> special method which is also known as constructor


#exceptional Handling

# class TooYoungException(Exception):
#     def __init__(self, x):
#         self.msg = x
        
# class TooOldException(Exception):
#     def __init__(self, x):
#         self.msg = x
        
# age = int(input("Enter age: "))
# if age > 60:
#     raise TooYoungException("Plz wait some more time... you will get best match")
# elif age < 18:
#     raise TooYoungException("Your age us already crossed marriage age.. No chance to getting marriage!")
# else:
#     print("You will get marraige details on email!")


f = open('abc.txt' , 'w')
f.write("Ambuj \n")
f.write("Software \n")
f.write("solutions \n")
f.close()


f = open('abc.txt' , "r")
data = f.read()
print(data)