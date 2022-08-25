import random
system=random.randint(0,99)
answere=99
answers=0
counter=1



while True:
   
    print("correct")  
    print("number is bigger")
    print("number is lower")
    
    useranswer = int(input())
    if useranswer== "correct":
        print("I am winner!")
        break
    elif useranswer== "number is bigger":
        answers=system 
        system=random.randint(answers+1,answere-1)
        counter+=1
        print(answers)
    elif useranswer== "number is lower":
        answere=system
        system=random.randint(answers+1,answere-1)
        counter+=1
        print(answere)
    else:
        print("Error!")