import random

def get_random(min, max):
  return random.randrange(min, max + 1)

def shuffle(arr):
  last_index = len(arr) - 1

  for i in range(len(arr)):
    swap_index = get_random(i, last_index)
    print("swap", i, swap_index)
    arr[i], arr[swap_index] = arr[swap_index], arr[i]

my_array = [0,1,2,3,4,5,6,7,8,9]
shuffle(my_array)
print(my_array)
