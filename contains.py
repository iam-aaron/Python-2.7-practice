#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser(description="Search for words including partial word")
parser.add_argument('snippet', help="partial (or complete) string to search for in the words file")

args = parser.parse_args()
snippet = args.snippet.lower()

words = open("/usr/share/dict/words").readlines() #dictionary in our machine

# APPROACH 1
# matches = []

# for word in words:
#     if snippet in word.lower():
#         matches.append(word.strip())
# print(matches)

# APPROACH 2 List comprehension
print([word.strip() for word in words if snippet in word.lower()]) #list comprehension version
