# Write a function for finding the index of the "rotation point," 
# which is where I started working from the beginning of the 
# dictionary. This array is huge (there are lots of words I don't know) 
# so we want to be efficient here.

words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote', # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage'
]

# lazy solution
# O(n)
def find_rotation_point(words):
    point = { 'word': '', 'index': 0 }
    for word in words:
        if point['word'] < word:
            point = { 'word': word, 'index': point['index'] + 1 }
        else:
            return point['index']

# O(logn)
# need to cut this guy in half somehow
def find_rotation_point_two(words):
    print(0)

res = find_rotation_point_two(words)
print(res)
