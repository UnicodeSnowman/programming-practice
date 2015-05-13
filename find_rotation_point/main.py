# Write a function for finding the index of the "rotation point," 
# which is where I started working from the beginning of the 
# dictionary. This array is huge (there are lots of words I don't know) 
# so we want to be efficient here.

_words = [ 'j','k','v','a','b','c','d','e','g','i' ]
__words = [ 'c','d','e','g','i','j','k','v','a', 'b' ]

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
# need to cut this guy in half somehow... binary search
def find_rotation_point_two(words):

    guess = 0
    start = 0
    end = len(words) - 1

    # our end condition surfaces when start and end are the only
    # elements left, of the form [start, *our-element*], meaning
    # that start + 1 == end == our-element
    while start + 1 < end:
        guess = (start + end) / 2

        if words[guess] > words[start]:
            start = guess
        else:
            end = guess

    return end

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

res = find_rotation_point_two(words)
print(res)
