# PEP278 - Universal  newlines in python 3.
# This feature translates simple \n to native new line sequence  for your
# platform on input and output.

from urllib.request import urlopen

with urlopen('http://sixty-north.com/c/t.txt') as story:
    print(type(story))
    words = []
    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            words.append(word)

print(words)

print("list comprehension ")

with urlopen('http://sixty-north.com/c/t.txt') as story:
    words = [line.decode("utf-8").split() for line in story]
print(words)
