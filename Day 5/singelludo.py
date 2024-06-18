

import random

position1 = 0

while True:
    input("Your turn Prabesh")
    roll = random.randint(1, 6) 
    

    print(f"You rolled a {roll} prabesh")  
    
    
    position1 += roll
    
   
    if position1 == 14:
        print("You landed on 14. Moving back to 3.")
        position1 = 3
    elif position1 == 17:
        print("You landed on 17. Moving back to 9.")
        position1 = 9
    elif position1 == 19:
        print("You landed on 19. Moving back to 7.")
        position1 = 7
    elif position1 == 24:
        print("You landed on 24. Moving back to 1.")
        position1 = 1
    elif position1 ==29:
         print("You landed on 29. Moving back to 2.")
         position1==2
    
    print(f"Your current position is {position1} Prabesh\n")
    
    if position1 >= 30:
        print("Congratulations! You've reached the end and won the game Prabesh!")
        break

