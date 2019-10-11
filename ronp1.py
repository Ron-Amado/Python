# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
""" 
#Name: Ron Amado
#Class: YA-4 ׁׂ(יא-4)


def InputDict():
    dict= {}
    for num in range(3):
        key= input("Enter a string ")
        value= int(input("Enter an integer number "))
        dict[key]=value
    return (dict)


def KeyInDict(dict1):
    key= input ("Enter a string ")
    if key in dict1:
        print ("YES!")
    else: 
        print ("NO!")
        

dict1= InputDict()
KeyInDict(dict1)