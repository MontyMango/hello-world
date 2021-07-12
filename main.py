from random import randint
from time import sleep

while True:
  number = randint(1,5)
  for i in "Hello world":
    print(number*'| ',i,end=' ')
    print(number*' |')
    sleep(.2)
  print("\n")
  sleep(1)
