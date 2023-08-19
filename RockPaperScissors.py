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

list=[rock,paper,scissors]

u_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(list[u_choice])
if(u_choice>2 and u_choice<0):
  print
  

print("Computer chose:")
c_choice=random.randint(0,3)
print(list[c_choice])

if(u_choice==c_choice):
  print("It's a draw.")
elif(u_choice==0 and c_choice==1):
  print("Computer Won!")
elif(u_choice==1 and c_choice==2):
  print("Computer Won!")
elif(u_choice==2 and c_choice==0):
  print("Computer Won!")
elif(u_choice==1 and c_choice==0):
  print("You Won!")
elif(u_choice==0 and c_choice==2):
  print("You Won!")
elif(u_choice==2 and c_choice==1):
  print("You Won!")
else:
  print("You lose")


