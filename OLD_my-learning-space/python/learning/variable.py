#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

# Print current directory
print(os.getcwd())

# Print name of current module, __main__ if script was call from shell and filename if module was import from an other python script
print(__name__)




tab = ['1','2','3','4','5']
dic = {'largeur':10,'longeur':5,'hauteur':3}

print(*tab)
print(*dic)

print(sys.argv)

if __name__ == '__main__':
	pass
	# Execution as script
else:
	pass
	# Execution as module 




def coolPrint():
	number = 5
	result = 0
	print(f"The result is {result} with number {number}")
	print("The result is {} with number {}".format(result, number))
	
