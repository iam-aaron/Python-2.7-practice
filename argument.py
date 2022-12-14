#!/usr/bin/python

#APPROACH 1
#import sys

#print("First argument %s" % sys.argv[0]) #first argument is the file itself, space separated


#APPROACH 2
# import argparse

# parser = argparse.ArgumentParser(description="Reads a file in reverse")
# parser.add_argument('filename', help="the file to read")
# parser.add_argument('--limit', '-l', type=int, help="the number of lines to read")
# parser.add_argument('--version', '-v', action='version', version="%(prog)s 1.0")

# args = parser.parse_args()

# with open(args.filename) as f:
#     lines = f.readlines()
#     lines.reverse() #modify the contents of the list

#     if args.limit:
#         lines = lines[:args.limit]

#     for line in lines:
#         print(line.strip()[::-1]) #[::-1] reverses the string


#APPROACH 2 with error handling
import argparse

parser = argparse.ArgumentParser(description="Reads a file in reverse")
parser.add_argument('filename', help="the file to read")
parser.add_argument('--limit', '-l', type=int, help="the number of lines to read")
parser.add_argument('--version', '-v', action='version', version="%(prog)s 1.0")

args = parser.parse_args()

try:
    f = open(args.filename)
except IOError as err: # set error type, WE CAN HAVE multiple except statement
    print("Error: file not found")
else:
    with f: 
        limit = args.limit
        lines = f.readlines()
        lines.reverse() #modify the contents of the list

        if limit:
            lines = lines[:limit]

        for line in lines:
            print(line.strip()[::-1]) #[::-1] reverses the string

finally: #this will always happen in try, usually we put here some cleanup steps like closing connections, etc.
    print("\nWe've finished\n")


