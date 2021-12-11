import  random

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

#Write your code below this line 👇



options = [rock, paper, scissors]

chioce = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if chioce >= 3 or chioce < 0:
  print("You printed the wrong number, you lose")
else:
  print(options[chioce])

  pc_chioce_rd = random.randint(0,2)
  print("Computer choice: ") 
  print(options[pc_chioce_rd])


#also elif chioce > pc_chioce_rd:
#print("You win")
  if chioce == 1 and pc_chioce_rd == 0 :
    print("Good, You win!")  
  elif chioce == 2 and pc_chioce_rd == 1 :
    print("You win!")
  elif chioce == 0 and pc_chioce_rd == 2 :
    print("You Win!")
  elif chioce == pc_chioce_rd:
    print("It's a draw")
  else:
    print("You lose, sorry!")