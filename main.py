#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sayan Mukherjee"
__version__ = "0.1.0"
__license__ = "MIT"

import unittest

def reverse(string):
    ''' takes a string as an argument and returns a new string which is the reverse of the argument w/o using built in reverse '''

    reverse_str = ''

    for idx in range(len(string)):
        reverse_str += string[len(string) - idx - 1]

    return reverse_str

def rev_enumerate(string):
    ''' start at the end of the sequence and return the elements in the sequence from last to first along with the corresponding offset '''

    for i in range(len(string)):
        yield len(string) - i - 1, string[len(string) - i -1]

def find_second(s1, s2):
    '''  returns the offset of the second occurrence of s1 in s2 '''

    return s2.find(s1, s2.find(s1) + 1)


def get_lines(file_name):
    ''' Opens a file for reading and returns one line from the file at a time.
        First combine lines that end with a backslash (a continuation) with the subsequent line or lines until a line is found that does not end with a backslash.   
        Also, removes all comments from the file where comments may begin with a '#' anywhere on the line and continue until the end of the line.  
        Also any line that begins with a comment is ignored and not returned. '''

    try:
        fp = open(file_name, 'r')
    except FileNotFoundError:
        print(file_name, "not found")
    else:
        with fp:
            statement = ''
            for line in fp:
                line = line.strip() # gets rid of newline in windows system

                if line.endswith('\\'):
                    statement += line.rstrip('\\')
                    # get next line w/o returning this one
                    continue
                else:
                    statement += line
                
                comment_starts = statement.find('#')
                # if statement contains '#' strip till that point, else get entire line
                last_idx = comment_starts if comment_starts > -1 else len(statement)
                
                yield statement[:last_idx]
                statement = ''

class AllTest(unittest.TestCase):
    ''' Test cases for all functions '''

    def test_reverse(self):
        ''' test reverse(string) '''

        self.assertEqual(reverse('hello'), 'hello'[::-1])
        self.assertEqual(reverse('hello world with space'), 'hello world with space'[::-1])
        self.assertEqual(reverse('madam racecar'), 'madam racecar'[::-1])
        self.assertEqual(reverse('0123456'), '0123456'[::-1])        
        self.assertEqual(reverse(''), ''[::-1])

    def test_rev_enumerate(self):
        ''' test rev_enumerate(string) '''

        test_seq = 'hello'
        self.assertEqual([(i, x ) for i, x in rev_enumerate(test_seq)], [(len(test_seq) -  i - 1, x ) for i, x in enumerate(test_seq[::-1])])
        test_seq = 'hi! Pythonista!'
        self.assertEqual([(i, x ) for i, x in rev_enumerate(test_seq)], [(len(test_seq) -  i - 1, x ) for i, x in enumerate(test_seq[::-1])])
        test_seq = [10, 20, 30, 40]
        self.assertEqual([(i, x ) for i, x in rev_enumerate(test_seq)], [(len(test_seq) -  i - 1, x ) for i, x in enumerate(test_seq[::-1])])
        test_seq = ''
        self.assertEqual([(i, x ) for i, x in rev_enumerate(test_seq)], [(len(test_seq) -  i - 1, x ) for i, x in enumerate(test_seq[::-1])])

    def test_find_second(self):
        ''' test find_second(s1, s2) '''

        self.assertEqual(find_second('iss','Mississippi'), 4)
        self.assertEqual(find_second('abba', 'abbabba'), 3)
        self.assertEqual(find_second('is', 'this is'), 5)
        self.assertEqual(find_second(' ', 'is it as'), 5)
        self.assertEqual(find_second('mad', 'madam'), -1)
        self.assertEqual(find_second('ISS','Mississippi'), -1)

    def test_get_lines(self):
        ''' test get_lines(file) '''
        result = ''
        
        for line in get_lines('test.txt'):
            result += line

        expected_result = '<line1 ><line2><line3.1 line3.2 line3.3><line4.1 line 4.2><line5><line6>'

        self.assertEqual(result, expected_result)

    
if __name__ == "__main__":
    ''' This is executed when run from the command line '''

    unittest.main(exit=False, verbosity=2)
