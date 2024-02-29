​
​
from collections import defaultdict
def anagrams(s1, s2):
  return charCount(s1)==charCount(s2)
​
def charCount(s):
  hash = defaultdict(int)
  for c in s:
    # if not c in hash:
    #   hash[c]=0
    hash[c]+=1
  return hash