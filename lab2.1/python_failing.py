#! /usr/bin/env python

"""
This program shows the implementation of int() and str(), where
a string can be converted to int (if possible) and an integer
can be converted to str (if possible).
Example:
    int_to_str(4)   --> "4"
    str_to_int("4") -->  4
Due to the nature of this program and its intentions, the input
string and/or integer will be defined in the main section within
this code.
"""
import sys

def check_inputs(input_str=False, input_int=False):
    if input_str:
        if not isinstance(input_str,str):
            raise AssertionError('Only strings can be converted to integers')
        if '.' in input_str:
            sys.exit('This program cannot convert strings to float type')
    if input_int:
        if not isinstance(input_int,int):
            raise AssertionError('Only integers can be converted to strings')

def int_to_str(input_int):
    check_inputs(input_int=input_int)
    int_str = ''
    negative = False
    if input_int < 0:
        input_int *= -1
        negative = True
    while input_int > 0:
        int_str += chr(ord('0') + input_int%10)
        input_int //= 10
    if negative:
        return (int_str + '-')[::-1]
    return int_str[::-1]

def str_to_int(input_str):
    check_inputs(input_str=input_str)
    str_int = 0
    negative = False
    if input_str[0] == '-':
        input_str = input_str[:0]+input_str[1:]
        negative = True
    dec_places = len(input_str)-1
    for char in input_str:
        str_int += (ord(char) - 48) * (10**dec_places)
        dec_places -= 1
    if negative:
        return str_int * -1
    return str_int


if __name__ == '__main__':
    input_int = 10
    input_str = '120'

    print("---- Integer to string ----")
    print("Integer: {}\nOriginal type: {}".format(input_int, type(input_int)))
    print("String: {}\nConverted type: {}".format(int_to_str(input_int),type(int_to_str(input_int))))

    print("---- String to integer ----")
    print("String: {}\nOriginal type: {}".format(input_str, type(input_str)))
    print("Integer: {}\nConverted type: {}".format(str_to_int(input_str),type(str_to_int(input_str))))
