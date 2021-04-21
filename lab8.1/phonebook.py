#! /usr/bin/env python

"""
This program manages a phone book (like the yellow pages). Saved data includes:
    - Name
    - Email
    - Age
    - Country of origin
Instances can be created or deleted, all data can be accessed by email and age,
and the full record can be displayed.
Since emails are unique, this will be the criteria for avoiding duplicates, deleting instances
and searching.
A text file will be generated each time.
"""
import os
import unittest
import logging

logging.basicConfig(level=logging.INFO)

if os.path.exists('registry.txt'):
    logging.info('Removing existing registry.txt to avoid conflicts')
    os.remove('registry.txt')

class PhoneBook():
    format_data = ['Name: ', 'Email: ', 'Age: ', 'Country: ']
    phonebook_file = 'registry.txt'
    def __init__(self):
        self.phone_book = dict()

    def add_new(self, name, email, age, country):
        phonebook_file = open(self.phonebook_file, "a+")
        self.phone_book[email] = [name, email, age, country]
        for i in range(4):
            phonebook_file.write(self.format_data[i] + self.phone_book[email][i] + '\n')
        phonebook_file.close()

    def delete(self, email):
        self.phone_book.pop(email, None)

    def show_one(self, email, test=False):
        try:
            self.phone_book[email]
        except:
            return self.phone_book
        if not test:
            for i in range(4):
                print(self.format_data[i], self.phone_book[email][i])
                return None
        return self.phone_book[email]

    def show_all(self):
       try:
          phonebook_file = open(self.phonebook_file, "r")
          print(phonebook_file.read())
          phonebook_file.close()
          return
       except:
           logging.error('No file has been generated')
           return


class TestPhoneBook(unittest.TestCase):

    newpb = PhoneBook()
    # (R & C) Right and
    def test_add_new(self):
        logging.info('Testing if new instances are added to phonebook')
        self.newpb.add_new('Daniela', 'daniela@email.com', '25', 'Mexico')
        self.assertTrue('Daniela' in self.newpb.show_one('daniela@email.com', test=True))
        self.newpb.add_new('Alejandra', 'alejandra@email.com', '25', 'Mexico')
        self.assertTrue('Alejandra' in self.newpb.show_one('alejandra@email.com', test=True))

    def test_delete(self):
        logging.info('Testing if existing instances can be deleted')
        self.assertTrue('daniela@email.com' in self.newpb.show_one('daniela@email.com', test=True))

    def test_show_one(self):
        logging.info('Testing if existing instances can be shown')
        self.newpb.delete('daniela@email.com')
        self.assertFalse('daniela@email.com' in self.newpb.show_one('daniela@email.com', test=True))

if __name__ == '__main__':
    unittest.main()
