# https://www.interviewcake.com/question/matching-parens

# I like parentheticals (a lot).
# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
# 
# Write a function that, given a sentence like the one above, along with the position of an opening parenthesis,
# finds the corresponding closing parenthesis.
# 
# Example: if the example string above is input with the number 10 (position of the first parenthesis),
# the output should be 79 (position of the last parenthesis).

sentence = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

def matching_paren_index(s, idx):
  if s[idx] is not "(":
    raise Exception("Character at index must be '('!")

  paren_count = 1
  for i in range(idx + 1, len(s)):
    if s[i] is "(":
      paren_count += 1
    elif s[i] is ")":
      paren_count -= 1

    if paren_count is 0:
      return i

  raise Exception("No closing paren for provided index!")

print(matching_paren_index(sentence, 10))
#print(matching_paren_index(sentence, 28))
#print(matching_paren_index(sentence, 57))
