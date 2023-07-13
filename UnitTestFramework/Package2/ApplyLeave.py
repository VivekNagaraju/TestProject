'''
Created on 11-Mar-2023

@author: iQuest02
'''
import unittest


class TestLeave(unittest.TestCase):


    def test_One_Leave(self):
        print("One leave applied")

    def test_Two_Leave(self):
        print("Two leaves applied")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()