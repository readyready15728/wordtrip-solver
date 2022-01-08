import itertools
import sys

dictionary = '/usr/share/dict/words'

with open(dictionary) as f:
    words = set(word.rstrip() for word in f.readlines())

letters = sys.argv[1]
possibilities = []

for i in range(2, len(letters) + 1):
    for p in itertools.permutations(letters, i):
        possibilities.append(''.join(p))

for p in possibilities:
    if p in words:
        print(p)
