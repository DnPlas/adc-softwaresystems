#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
This program parses a text file (given as parameter) and
returns the number of ocurrences of a word(s) identified
in the file. The word(s) to identify is received as a 
parameter, the detection is case sensitive and the program
works any language where words are separated by spaces or
punctuation marks (UTF-8). Beware, the output may not show
unicode characters due to UTF-8 encoding/decoding limitations.
This program will match punctuations and the word before
punctuation marks , but will not match them together. Exmaple:
    - !, will match all the occurences of !
    - mark, will match all occurrences of mark
    - mark!, will not match mark!
The program will count numbers as well.
"""

import os
import re
import sys


word_count = dict()
words = []

def get_input():
    try:
        file_name = sys.argv[1]
        word_list = sys.argv[2:]
        if file_name and word_list:
            return file_name, word_list
        sys.exit(0)
    except:
        sys.exit('Both a file name and a word(s) are required\nExiting')

def parse_file(file_name):
    for line in file_name:
        line = line.strip()
        l_split = re.split('(\W)', line)
        for w in l_split:
            words.append(w)
    return words

def count_words(words, word_count, word_list):
    if not set(word_list)&set(words):
        sys.exit('None found\nExiting')
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else: word_count[word] = 1
    return word_count
def open_file(file_name):
    try:
        text = open(file_name, 'r', encoding='utf-8')
        size = os.path.getsize(file_name)
        if size == 0:
            sys.exit('Empty file\nExiting')
        return text
    except OSError:
        sys.exit('File not found\nExiting')

if __name__ == '__main__':
    file_name, word_list = get_input()
    text = open_file(file_name)
    count_dict = count_words(parse_file(text), word_count, word_list)
    for word in word_list:
        try:
            print(word, ':', count_dict[word])
        except:
            print(word, ':', 0)
    sys.exit(0)
