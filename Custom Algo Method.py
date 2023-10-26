import numpy as np
import random as rand

guessMax = rand.randint(0, 500)
checkList = []

#Usually provided on LeetCode or other white boarding sites
for x in range(guessMax): 
  checkList.append(x)
  np.random.shuffle(checkList)

target = rand.choice(checkList)
#print("Before: ", checkList)


#Solution Code
while True:
  guessRand = rand.choice(checkList)
  if guessRand == target:
    print(target)
    break
  
  if guessRand > target:
    for x in checkList:
      if guessRand <= x: 
        checkList.remove(x)
        
  if guessRand < target:
    for x in checkList:
      if guessRand >= x: 
        checkList.remove(x) 
