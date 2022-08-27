from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

print("Welcome to the secret auction program. ")
first_name=input("What's your name? ")
first_num=int(input("What's your bid? "))
finish=False
bid_dic={}
bid_dic[first_name]=first_num
choice=input("Are there any other bidders? Type 'yes' or 'no' ")

if choice == "yes":
  finish= False

else:
  finish=True
  
clear()

while (finish == False):
  name=input("What's your name? ")

  value=int(input("What's your bid? "))

  bid_dic[name]=value

  choice=input("Are there any other bidders? Type 'yes' or 'no' ")

  if choice == "yes":
    finish= False

  else:
    finish=True

  clear()
    
max=0
for key in bid_dic:
  if bid_dic[key] > max:
    max=bid_dic[key] 

for key in bid_dic:
  if bid_dic[key] == max:
    print("Winner is " + key + " with a bid of " + str(bid_dic[key]) + " ")