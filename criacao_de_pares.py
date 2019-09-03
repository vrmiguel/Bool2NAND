#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:45:43 2019

@author: vinicius
"""
'''
strcnf = "(A | B | ~C) & (B | C | ~A)"
splitcnf = strcnf.split("&") # Divide a string de forma normal conjuntiva em substrings somente com operações OR
splitcnf = [x.strip() for x in splitcnf] # Remove espaços no começo e fim de cada substring
print(splitcnf) '''

z1 = ['A', 'B', 'C', 'D', 'E']
z2 = ['A', 'B', 'C', 'D', 'E', 'F']
z3 = ['A', 'B', 'C', 'D', 'E', 'F', 'H']

def concatenar_pares(z):
    z_c = [z[i] + z[i+1] for i in range(0, len(z)-1, 2)]
    if len(z) % 2 != 0:
        z_c += z[-1]
    print(z_c)
     

concatenar_pares(z1)
print("------------------------")
concatenar_pares(z2)
print("------------------------")
concatenar_pares(z3)
