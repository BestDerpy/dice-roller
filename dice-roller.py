def diceroll(dice):
  import re
  import random

  m = 0
  n = 0
  result = 0

  if bool(re.match(r"^[1-9]?\d[dD]([1-9]?\d|100)?$", dice)) and not bool(re.match(r"^\d+[dD]1$", dice)):
    cast = re.split("[dD]", dice)
    m = int(cast[0])
    n = int(cast[1])
  else:
    print("Your dum")
  
  while m > 0 and n > 0:
    result += random.randint(1, n)
    m -= 1
  print(result)

print('Dice Rolling Simulator')
print("Enter dice to roll in this format (mDn, where 'm' is the number of dice and 'n' is the sides of the dice.)")
print('Press Q to exit: \n')
while True: 
  inputStr = input("Type a dice to roll: ")
  if inputStr.lower() == "q": 
    break
  diceroll(inputStr)