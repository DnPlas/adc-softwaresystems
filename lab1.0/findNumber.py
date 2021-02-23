#! /usr/env/bin python

"""
This program generates random numbers [1,30] and
asks the user to guess the number. It is invoked from the
command line and outputs the following messages:
    - TOO HIGH, if input number is above target
    - TOO LOW, if input number is below target
    - RIGHT!, if input number is target
To exit the game, the user has to guess right or type exit in the command line.
"""
import sys
import random as rand

from datetime import datetime as dt

rand.seed()
target = rand.randrange(1,30)
tries = 0
tries_log = open("GuessingSteps.txt", "a+")

def get_input():
    usr_in = input('Please enter your guess: ')
    if usr_in == 'exit':
        sys.exit('Exiting')
    return int(usr_in)

def check_in(target, usr_in, tries):
    if target == usr_in:
        print('RIGHT\nTries:', tries)
        timestamp = dt.now()
        tries_log.write("\n---- Game on: " + str(timestamp))
        tries_log.write("\nTries: %d" % tries)
        sys.exit('Exiting')
    elif usr_in > target:
        msg = 'TOO HIGH'
    elif usr_in < target:
        msg = 'TOO LOW'
    return msg

if __name__ == '__main__':
    print('Welcome to the guessing game! Enter digits ONLY')
    msg = True
    while (msg):
        usr_in = get_input()
        tries += 1
        msg = check_in(target, usr_in, tries)
        print(msg)

