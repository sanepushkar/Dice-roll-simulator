import random

print ("How many dice?")
number_dice = int(input())

roll_again = input("Do you want to roll the dice?")
roll_again=='yes'
while roll_again =='yes'or roll_again=='y':
  print('Rolling the dice.....')
  print ('The number is')
  if number_dice == 1:
    print (random.randint(1, 6))
  if number_dice == 2:
    print (random.randint(1, 6))
    print (random.randint(1, 6))
  if number_dice > 2:
    print("This game can only be played with 2 dice")

  roll_again = input("Do you want to roll again?")


