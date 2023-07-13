'''
Created on 11-Mar-2023

@author: iQuest02
'''
import unittest


class TestLogin(unittest.TestCase):


    def test_Positive(self):
        print("Positve login test case")
        self.assertTrue(False, "Test failed")
        
    def test_Negative(self):
        print("Negative login test case")
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()