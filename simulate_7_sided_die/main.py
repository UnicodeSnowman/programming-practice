# https://www.interviewcake.com/question/simulate-7-sided-die?utm_source=weekly_email
# You have a function rand5() that generates a random integer from 1 to 5.
# Use it to write a function rand7() that generates a random integer from 1 to 7.
# rand5() returns each integer with equal probability. rand7() must also return each integer with equal probability.

from random import random
from math import floor

def rand5():
  return floor(random() * 5) + 1

def rand7():
  # we need at least two calls to rand5 in order to generate a rand7. what are our valid cases? well, with two "rolls" or rand5,
  # we have 5 * 5 = 25 possibilities, but for a random 1..7 number, our total number of outcomes needs to be divisible by 7
  # we can *try* to evenly distribute our 1..7 nums in our 25 possible slots
  #  results = [
  #      1, 2, 3, 4, 5,
  #      6, 7, 1, 2, 3,
  #      4, 5, 6, 7, 1,
  #      2, 3, 4, 5, 6,
  #      7, 1, 2, 3, 4
  #  ]
  # ... so any of these results from index 1..21 are valid, whereas results 22, 23, 24, and 25 are invalid. we need to choose
  # one of these, but throw away any results greater than index 21

  while True:
    # (5 - 1) * 5 + (5 - 1) + 1 = 20 + 4 + 1 = 25 => max case
    # (1 - 1) * 5 + (1 - 1) + 1 = 0 + 0 + 1 = 1 => min case
    # meaning we can get any number between 1 and 25
    result = (rand5() - 1) * 5 + (rand5() - 1) + 1

    if result <= 21:
      # got a number 1..21, we translate this into a number between 0 and 6, then adjust by 1 to get 1..7
      return result % 7 + 1


res = rand7()
print(res)

