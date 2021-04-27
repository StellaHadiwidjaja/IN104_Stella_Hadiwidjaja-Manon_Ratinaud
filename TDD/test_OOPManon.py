# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 17:54:17 2021

@author: a2ste
"""

import OOPManon
import unittest

class TestBooks(unittest.TestCase):
    ThreeBodyProblem = OOPManon.Books("ThreeBodyProblem","Cixin Liu") 
    
    def test_getTitle(self):
        self.assertEqual(OOPManon.Books.getTitle(), "ThreeBodyProblem")
     
    
    def test_initTheater(self):
        
        p = OOPManon.book2
        
        if isinstance(p.year, int):
            print('There is a problem with the types of variables: str int')
            raise TypeError
            
        if p.year>2020:
            print('Hmmm, this piece has not been written yet')
            

if __name__ == '__main__':
	unittest.main()


    