import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
choice=input("")

if int(choice) == 0:
    print(rock)

elif int(choice) == 1:
    print(paper)

elif int(choice) == 2:
    print(scissors)

print("Computer chose:")

comp_choice=random.randint(0,2)
if comp_choice == 0:
    print(rock)

elif comp_choice == 1:
    print(paper)

elif comp_choice == 2:
    print(scissors)


if int(choice)==0:
    if comp_choice ==2:
        print("You Win")
    
    elif comp_choice == 0:
        print("You Draw")
    
    else:
        print("You Lose")

elif int(choice)==2:
    if comp_choice ==1:
        print("You Win")    
    
    elif comp_choice==2:
        print("You Draw")
    
    else:
        print("You Lose")

elif int(choice) == 1:
    if comp_choice ==0:
        print("You Win")    
    
    elif comp_choice==1:
        print("You Draw")
        
    else:
        print("You Lose")
        


    

