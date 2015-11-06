# https://www.interviewcake.com/question/simulate-5-sided-die?utm_source=weekly_email

# You have a function rand7() that generates a random integer from 1 to 7.
# Use it to write a function rand5() that generates a random integer from 1 to 5.
# rand7() returns each integer with equal probability. rand5() must also return each integer with equal probability.

from random import random
from math import floor

def rand_7():
  return floor(random() * 7) + 1

def rand_5():
  rando = rand_7()
  while rando > 5:
    rando = rand_7()
  return rando

print(rand_5())
