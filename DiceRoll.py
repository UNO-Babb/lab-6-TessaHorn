#DiceRoll.py
#Name: Tessa Horn
#Date: 10/01/25
#Assignment: Lab 6 Dice Roll
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  for r in range(100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    rolls[total - 2] += 1 
    
  #find the sum total of the two dice
  
  #print statictics for dice rolls
  dicesum = 2
  for count in rolls:
   print(dicesum, ":", count)
   dicesum = dicesum + 1
 
  

if __name__ == '__main__':
  main()
