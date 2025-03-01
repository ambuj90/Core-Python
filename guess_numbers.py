import random

target = random.randint(1,100)   


while True:
    userChoice = input("Guess the target or Quit(Q) : " )
    if(userChoice == "Q"):
        break
    
    userChoice = int(userChoice)  
    if(userChoice == target):     
        print("Sucess: Correct Guess!")
        break
    elif(userChoice < target):     
        print("choose bigger number and guess again")
    else:  
        print("number is big, choose smaller")
    
print("Game Over")    
