#!/home/mayur/anaconda2/bin/python
# -*- coding: utf-8 -*-
# file: fact.py (practice file.)

from sys import argv
import math

def factorial(n):
	if n==1:
		return 1
	else:
		return n*factorial(n-1)

scriptName, number = argv

print factorial(int(number))
