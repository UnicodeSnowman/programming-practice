# I'm making a search engine called MillionGazillion™.
# I wrote a crawler that visits web pages, stores a few keywords in a database, and follows links to other web pages. I noticed that my crawler was wasting a lot of time visiting the same pages over and over, so I made a hash table visited where I'm storing URLs I've already visited. Now the crawler only visits a URL if it hasn't already been visited.
# 
# Thing is, the crawler is running on my old desktop computer in my parents' basement (where I totally don't live anymore), and it keeps running out of memory because visited is getting so huge.
# 
# How can I trim down the amount of space taken up by visited?

from functools import reduce

### deep merge
def merge(source, destination):
    """
    run me with nosetests --with-doctest file.py

    >>> a = { 'first' : { 'all_rows' : { 'pass' : 'dog', 'number' : '1' } } }
    >>> b = { 'first' : { 'all_rows' : { 'fail' : 'cat', 'number' : '5' } } }
    >>> merge(b, a) == { 'first' : { 'all_rows' : { 'pass' : 'dog', 'fail' : 'cat', 'number' : '5' } } }
    True
    """
    for key, value in source.items():
        if isinstance(value, dict):
            # get node or create one
            node = destination.setdefault(key, {})
            merge(value, node)
        else:
            destination[key] = value

    return destination

def main(url):
  visited = {
      'www': {}
  }

  www_index = url.find('www.')
  if www_index is not -1:
    visited['www'][url.split('www.')[1]] = True

  print(visited)

# if storing in this way, we are O(x^n), where x is the number of possible
# characters in a URL... i.e. 26 for only alphabetic lowercase, etc.
def main_2(url):
  def iter(acc, val):
    temp = {}
    temp[val] = acc
    return temp

  return reduce(iter, url[::-1], True)

url = 'www.google.com'
url2 = 'www.tester.com'
res = main_2(url)
res2 = main_2(url2)

print(merge(res, res2))
