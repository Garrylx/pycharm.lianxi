# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:55:10 2021

@author: gaoyuan
"""

def palindrome_filter(sentence):
    if len(sentence) > 0:
        tmp = sentence[0]
        if tmp.isalpha() == True:
            tmp = tmp.lower()
            return tmp + palindrome_filter(sentence[1:])
        else:
            return palindrome_filter(sentence[1:])
        
    else:
        return ""
    
    

def is_palindrome(sentence):
    if len(sentence) > 2:
        if sentence[0] == sentence[-1]:
            return is_palindrome(sentence[1:-1])
        else:
            return False
    elif len(sentence) == 2:
        if sentence[0] == sentence[1]:
            return True
        else:
            return False
    else:
        return True
        
    
    
    
    
    
print(palindrome_filter("Able was I ere I saw Elba."))
print(is_palindrome(palindrome_filter("Able was I ere I saw Elba.")))