#! /usr/bin/env python

"""
This program takes as input parameter a decimal integeer (0 + positive integers) and then
it displays the corresponding number in Binary and Hexadecimal.
Both the binary and hexadecimal converters are implemented.
"""

import sys

bin_conv = ''
hex_conv = ''
hex_dig = '0123456789ABCDEF'

def get_input():
    try:
        usr_in = int(input('Please enter a decimal integer or 0: '))
        return usr_in
    except ValueError:
        print("ONLY decimal integers are accepted, try again")
        return get_input()

def dec_bin(usr_in, bin_conv):
    if usr_in == 0:
        bin_conv += '0'
        return bin_conv[::-1]
    rem = str(usr_in%2)
    bin_conv += rem
    usr_in = usr_in//2
    return dec_bin(usr_in, bin_conv)

def dec_hex(usr_in, hex_conv):
    div = usr_in//16
    div_f = usr_in/16
    rem = int((div_f - div)*16)
    hex_conv += hex_dig[rem]
    if usr_in >= 16:
       return dec_hex(div, hex_conv)
    return hex_conv[::-1]

if __name__ == '__main__':
   print('Decimal to Binary and Hexadecimal converter')
   usr_in = get_input()
   print("Decimal: ", usr_in)
   print("Binary CALC: ", dec_bin(usr_in, bin_conv))
   print("Binary PYTH: ", bin(usr_in))
   print("Hexadecimal CALC: ", dec_hex(usr_in, hex_conv))
   print("Hexadecimal PYTH: ", hex(usr_in))
   sys.exit(0)
