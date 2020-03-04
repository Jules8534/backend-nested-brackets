#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: One line description of what your program does.
"""
__author__ = "Julita, Joshua, and Demo"

import sys
openers = [ '[', '(', '<', '{', '(*']
closers = [ ']', ')', '>', '}', '*)']


def is_nested(line):

    stack = []
    token_counter = 0
    while line:

        token = line[0]
        if line.startswith("(*"):
            token = "(*"
        elif line.startswith("*)"):
            token = "*)"

        token_counter += 1
        line = line[len(token):]

        if token in openers:
            stack.append(token)
        elif token in closers:
            closer_index = closers.index(token)
            expected_opener = openers[closer_index]
            if stack.pop() != expected_opener:
                return "NO " + str(token_counter)        
    
    if stack:
            
            return "NO " + str(token_counter)

    return "YES"
        
    
def read_file(filename):
    with open(filename, 'r') as f:
        for string in f:
            is_nested(string)

    

def main(args):
    """Open the input file and call `is_nested()` for each line"""
    
    print("Testing for Nesting: {}".format(args[0]))
    with open(args[0]) as ifile:
        with open('output.txt', 'w') as ofile:
            for line in ifile:
                result_str = is_nested(line)
                print(result_str)
                ofile.write(result_str + '\n')




if __name__ == '__main__':
    main(sys.argv[1:])

