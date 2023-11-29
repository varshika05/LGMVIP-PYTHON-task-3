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
game_on = True

while game_on:
  userPick = input("what sign do you pick? Type 0 rock, 1 for paper or 2 for scissors. ")

  if int(userPick) not in range(3):
    print('Invalid choice')
    continue

  signs = [rock, paper, scissors]

  signPicker = random.randint(0, 2)

  computerSign = signs[signPicker]
  userSign = signs[int(userPick)]

  print('You chose:')
  print(userSign)

  print('Computer chose:')
  print(computerSign)

  if userPick == "0":
    if signPicker == 0:
      print("It's a tie!")
    elif signPicker == 1:
      print("You lose!")
    elif signPicker == 2:
      print('You win!')

  elif userPick == "1":
    if signPicker == 1:
      print("It's a tie!")
    elif signPicker == 2:
      print("You lose!")
    elif signPicker == 0:
      print('You win!')

  elif userPick == "2":
    if signPicker == 2:
      print("It's a tie!")
    elif signPicker == 0:
      print("You lose!")
    elif signPicker == 1:
      print('You win!')

  while True:
    play_again = input('Play Again? Y for no or N for no\n').lower()
    if play_again == 'y':
      break
    elif play_again == 'n':
      game_on = False
      break
    else:
      print('invalid choice')
      continue

print('Game Over')

