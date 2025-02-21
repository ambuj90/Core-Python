fruits = ["banana", "apple", "cherry"]
print(fruits[0])
print(fruits[-1])
print(fruits[2])

#List Slicing

numbers = [2, 5, 4, 8, 9, 2, 3]
print(numbers[1:5])
print(numbers[:5])
print(numbers[-2:])

#Modifying Lists
list = ["a", "b", "c", "d"]
list[1]="f"
print(list)

#Adding Elements

name = ["ambuj", "rachit", "rohit", "sagar"]
name.append( "sunil")
print(name)

name.insert(3,"sunil")
print(name)

#Removing Elements

name.remove("sunil")
print(name)

name.pop(1)
print(name)

del name[0]
print(name)

name.clear()
print(name)


#Sorting & Reversing

nums = [2, 5, 8, 9, 6 , 7]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

nums.reverse()
print(nums)