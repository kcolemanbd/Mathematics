#!/usr/bin/python3

'''
Created on Dec 3, 2016

@author: keithcoleman
This is a simple prime number generator that finds prime numbers within a user defined range.  A great script to use with the RSA scripts
'''


   
def primeNumberFinder(p=1): 
    while(True): 
        if primeFilter(p): yield p
        p+=1
        
def primeFilter(n):
    if n==1:return False
    for x in range(2,n): return False if n%x==0 else True
            
def main(minNumber,maxNumber):    
    for minNumber in primeNumberFinder():
        if minNumber>maxNumber: break
        print(minNumber)
    
    
if __name__ == '__main__':
    print("This program finds prime numbers within a user defined range")
    minPrime=input("Please enter the starting value:")
    maxPrime=input("Please enter the ending value:")
    try:
        main(minPrime,maxPrime)
    except BaseException as e:
        print("We have a problem ({})".format(e))
