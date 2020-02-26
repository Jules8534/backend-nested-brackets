#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
#__author__ = Julita, Joshua

import sys
open_b =[ '[', '(', '<', '{', '(*']
closed_b = [ ']', ')', '>', '}', '*)']


def is_nested2(line):
    stack = []
    i = 0
    #(*a++(*)
    while i < len(line):
        if i+2 < len(line) and line[i: i+2] in open_b:
            stack.append(line[i: i+2])
            i += 1
        elif i + 2 < len(line) and line[i:i+2] in closed_b:
            if len(stack) == 0:
                print("No", i)
                return
            tem = stack.pop()
            if open_b.index(tem) != closed_b.index(line[i:i+2]):
                print("No", i)
                return
            i += 1
        elif line[i] in open_b:
            stack.append(line[i])
        elif line[i] in closed_b:
            if len(stack) == 0:
                print("No", i)
                return
            tem =  stack.pop()
            if open_b.index(tem) != closed_b.index(line[i]):
                print("No", i)
                return
        i += 1
        
    if len(stack) > 0:
        print("No", i)
    else:
        print("Yes")

# def is_nested(line):
#     """Validate a single input line for correct nesting"""
#     current_brackets =[]
#     temp_index = [] #this will let us know where the closing bracket has an opener
#     index = 0 #this will let us know where it broke
#     while line:
#         if len(line) > 1:
#             if line[0] + line[1] in open_b:
#                 current_brackets.append(line[0] + line[1])
#                 temp_index.append(open_b.index((line[0] + line[1])))
#                 line = line[2:]
#                 index += 1
#             elif line[0] in open_b:
#                 current_brackets.append(line[0])
#                 temp_index.append(open_b.index(line[10]))
#                 line = line[1:]
#             elif line[0] + line[1] in closed_b:
#                 if temp_index[-1] == closed_b.index(line[0] + line[1]):
#                     temp_index.pop()
#                     current_brackets.pop()
#                     line = line[2: ]
#                     index +=1
#                 else:
#                     break
#             elif line[0] in closed_b:
#                 if temp_index[-1] == closed_b.index(line[0]):
#                     temp_index.pop()
#                     current_brackets.pop()
#                     line = line[1: ]
#                     index += 1
#                 else:
#                     break
#             elif line[0] not in closed_b and line[0] not in open_b:
#                 line = line[1: ]
#                 index += 1
#             elif len(line[0]) == open_b:
#                 current_brackets.append(line[0])
#                 line = line[1:]
#                 index += 1
#             elif line[0] in closed_b:
#                 if temp_index[-1] == closed_b.index(line[0]):
#                     temp_index.pop()
#                     current_brackets.pop()
#                     line = line[1: ]
#                     index +=1
#                 else:
#                     break
#             elif line[0] not in closed_b and line[0] not in open_b:
#                 line = line[1: ]
#                 index += 1
#         f = open("output.txt" , "a+")
#         if len(current_brackets) == 0:
#             print("YES")
#             f.write("YES \n")
#             f.close()
#         else:
#             print('NO' + ' ' + str(index+1))
#             f.write('NO' + ' ' + str(index+1) + '\n')
#             f.close()

def read_file(filename):
    with open(filename, 'r') as f:
        for string in f:
            is_nested2(string)



    


def main(args):
    """Open the input file and call `is_nested()` for each line"""
    # Results: print to console and also write to output file
    if len(args) !=2:
       print('usage: python nested.py input.txt')
       sys.exit(1)
    #read_file("input.txt")
    


if __name__ == '__main__':
    main(sys.argv)

