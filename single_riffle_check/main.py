# https://www.interviewcake.com/question/single-rifle-check
import math

deck = list(range(1, 53))

def is_single_riffle(shuffled_deck, half1, half2):
  if len(shuffled_deck) == 0:
    return True

  if len(half1) > 0 and shuffled_deck[0] is half1[0]:
    return is_single_riffle(shuffled_deck[1:], half1[1:], half2)
  elif len(half2) > 0 and shuffled_deck[0] is half2[0]:
    return is_single_riffle(shuffled_deck[1:], half1, half2[2:])
  else:
    return False

def is_single_riffle_optimized(shuffled_deck=[], half1=[], half2=[]):
  def iter(sd_i, h1_i, h2_i):
    if sd_i > len(shuffled_deck) - 1:
      return True

    if h1_i <= len(half1) - 1 and shuffled_deck[sd_i] is half1[h1_i]:
      return iter(sd_i + 1, h1_i + 1, h2_i)
    elif h2_i <= len(half2) - 1 and shuffled_deck[sd_i] is half2[h2_i]:
      return iter(sd_i + 1, h1_i, h2_i + 1)
    else:
      return False

  return iter(0, 0, 0)

# even better, since we *always* take a card off of shuffled_deck with each pass, we could iterate through them instead,
# rather than recursing, thus saving some space

