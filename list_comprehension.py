#!/usr/bin/env python



# prints all the odd numbers in the list
# from traceback import print_list


# print("------------------------------------")
# print("LIST COMPREHENSION SAMPLE")
# num_range = range(10)
# print([item for item in num_range if item % 2 == 1])

# print("------------------------------------")
# print("PROMPT SAMPLE")

# def input_positive_integer(prompt):
#     while True:
#         input_val = int(input(prompt))
#         if input_val > 0:
#             return input_val

# user_input = input_positive_integer("Enter a positive integer: ")
# print('%i' % user_input)

# print("------------------------------------")
# print("USING TERNARY OPERATOR")

# input_num = int(input("Write a number: "))
# msg = "EVEN" if input_num%2 == 0 else "ODD"
# print(msg)


# print("------------------------------------")
# print("ENUMERATE")

# colors = {"red", "orange", "yellow", "green", "blue", "indigo", "violet"}

# for counter, color in enumerate(colors, 1): #enumerate method needs the iterable (list, tuple, dict) and starting count
#     print("#%i %s" % (counter, color))


# print("------------------------------------")
# print("FIND MISSING NUMBER")

# lst = [2,5,1,4,9,6,3,7]

# lower_bound = 1;
# upper_bound = 9

# rng = range(lower_bound, upper_bound)
# print([val for val in rng if val not in lst])


# print("------------------------------------")
# print("LAMBDA AND REDUCE")

# from functools import reduce

# lst = [2,1,3,-2]
# sum_of_all = reduce(lambda x,y: x+y, lst)

# print(sum_of_all)


# print("------------------------------------")
# print("PICK YOUR SIGN")
# from itertools import product
# lst = [2,1,3,-2]


# arr = [(x, -x) for x in lst]
# for t in product(*arr):
#     print(t)

#OR

# for t in product(*((x, -x) for x in lst)):
#         print(t)

# print("------------------------------------")
# # print("GET SUBSET OF INDEXES")

# indx=[0,5,7] # index list
# a = ['a', 'b', 3, 4, 'd', 6, 7, 8]

# indx.append(len(a))
# for i, j in zip(indx, indx[1:]):
#     print("%i, %i" % (i, j))


# print([a[i:j] for i, j in zip(indx, indx[1:])])


# print("------------------------------------")
# # print("GET COMBINATION OF LIST")


# from functools import reduce
# from itertools import combinations

# lst = [2,1,3,-2]

# lst_combination = list()
# goal = 4

# for n in range(len(lst)+1):
#     lst_combination += combinations(lst,n)    
    
# print(lst_combination)

# # selected_lst = [l for l in lst_combination if reduce(lambda x,y: x+y, l) == goal]
# selected_lst = [list(l) for l in lst_combination if len(l)>=2 and reduce(lambda x,y: x+y, l)==goal]

# print('\n'.join(map(str, selected_lst)))

import numpy
import warnings

data1 = []
# try: 
#     print(numpy.median(data1))
# except Warning as r:
#     print("Error in getting median")
#     exit(1)

with warnings.catch_warnings():
    warnings.filterwarnings('error')
    try:
        print(numpy.median(data1))
    except Warning as e:
        print("Error in getting median")
        exit(1)

