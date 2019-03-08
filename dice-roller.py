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