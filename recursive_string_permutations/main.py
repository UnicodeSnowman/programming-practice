def string_permutations(string):
  def get_permutations(prefix, chars):
    if len(chars) is 0:
      return [prefix]
    else:
      permutations = []
      for (idx, char) in enumerate(chars):
        permutations += get_permutations(prefix + [char], chars[:idx] + chars[idx + 1:])
      return permutations

  return get_permutations([], list(string))

sp = string_permutations("ABCD")

print(len(sp))
for item in sp:
  print(item)
