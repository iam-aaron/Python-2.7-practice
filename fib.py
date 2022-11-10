#!/usr/bin/env python

from argparse import ArgumentParser

def fib(n):
    if n in {0,1}:
        return n
    else:
        return fib(n-1)+fib(n-2)

parser = ArgumentParser(description="Generates the Fibonnaci sequence from the range given")
parser.add_argument("--range","-r",default=10,help="Give range to generate a Fibonacci sequence")

arg = parser.parse_args()

for iterator in range(int(arg.range)):
    print("[%i] %i" %(iterator+1, fib(iterator)))

# print('\n'.join(map(str,[fib(n) for n in range(int(arg.range))])))