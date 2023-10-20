import numpy as np
import random as rand

guessMax = rand.randint(0, 500)
target = rand.randint(0, guessMax)
guessAmount = 0
checkList = []

#Usually provided on LeetCode
for x in range(guessMax): 
  checkList.append(x)
  np.random.shuffle(checkList)

#Solution Code
while True:
  guessRand = rand.choice(checkList)
  guessAmount += 1
  if guessRand == target:
    print("It took ", guessAmount, " tries to get ", target)
    break
  
  if guessRand > target:
    for x in checkList:
      if guessRand <= x: 
        checkList.remove(x)
        
  if guessRand < target:
    for x in checkList:
      if guessRand >= x: 
        checkList.remove(x)

print(checkList)
