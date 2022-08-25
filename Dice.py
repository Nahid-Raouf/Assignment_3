import random  
Total = []

while True:
    dice = random.randint(1 , 6)
    Total.append(dice)  
    if dice == 6:
        continue
    
    else:
        print("Sum: ", (str(sum(Total))) + "List : ", (str(Total)))
        break

