

def gen_letter_map(string):
  results_map = {}
  for letter in string:
    results_map[letter] = results_map.get(letter, 0) + 1
  return results_map

# initial decent but annoyingly complex version
def is_palindrome_permutation(string):
  results_map = gen_letter_map(string)
  if len(string) % 2 is 0:
    for key, value in results_map.items():
      if value % 2 is not 0:
        return False
    return True
  else:
    odd_letter = None
    odd_count = 0
    even_count = 0
    for key, value in results_map.items():
      if value % 2 is 0:
        even_count += 1
      else:
        if odd_letter is None:
          odd_letter = key
          odd_count += 1
        elif odd_letter is key:
          odd_count += 1
        else:
          return False

    if even_count % 2 == 0 and odd_count % 2 == 1:
      return True
    return False

# better implementation... simply flip a boolean when we see a character. initially
# True for odd, then flip to False for even when we see it again
def is_palindrome_permutation_better(string):
  parity_map = {}
  for char in string:
    if char in parity_map:
      parity_map[char] = not parity_map[char]
    else:
      parity_map[char] = True # is odd initially

  has_odd = False
  for char, is_odd in parity_map.items():
    if is_odd:
      if has_odd:
        return False
      else:
        has_odd = True

  return True

civic = "civic"
ivicc = "ivicc"
civil = "civil"
livci = "livci"

for result in map(is_palindrome_permutation_better, [civic, ivicc, civil, livci]):
  print(result)
