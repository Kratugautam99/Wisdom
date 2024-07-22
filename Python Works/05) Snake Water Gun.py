import random 
def playSWGgame():
  print('Game will be played between you and computer and will be of 10 points')
  upts=0
  comppts=0
  while upts < 10 and comppts < 10:
    print("yours points : ", upts)
    print("computer points : ", comppts)
    user = str(input("Enter snake, water or gun : "))
    output = ('snake', 'water', 'gun')
    computer = random.choice(output)
    if user == computer:
      print(f"Draw as both chose the {user}")
    elif user == "snake" and computer == "water":
      print(f"computer chose {computer} and you chose {user}")
      print("You win as snake drinks water")
      upts+=1
    elif user == "snake" and computer == "gun":
      print(f"computer chose {computer} and you chose {user}")
      print("You lose as gun kills snake")
      comppts+=1
    elif user == "water" and computer == "snake":
      print(f"computer chose {computer} and you chose {user}")
      print("You lose as snake drinks water")
      comppts+=1
    elif user == "water" and computer == "gun":
      print(f"computer chose {computer} and you chose {user}")
      print("You win as water rusts gun")
      upts+=1
    elif user == "gun" and computer == "snake":
      print(f"computer chose {computer} and you chose {user}")
      print("You win as gun kills snake")
      upts+=1
    elif user == "gun" and computer == "water":
      print(f"computer chose {computer} and you chose {user}")
      print("You lose as water rusts gun")
      comppts+=1
    else:
      print("Invalid Input")
  if upts == 10:
    print('user winner')
  elif comppts == 10:
    print('computer winner')
dy = str(input("Do you want to play the game? - "))
if dy == "Yes" or dy == "yes":
  playSWGgame()
elif dy == "No" or dy == "no":
  print("ok see you later")
else:
  print(f"Answer should be in Yes or No and Your Input was {dy}.")
