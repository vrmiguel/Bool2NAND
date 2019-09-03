# -*- coding: utf-8 -*-
"""
github.com/vrmiguel/Bool2NAND
Ternary boolean expression into NANDs
"""

from sympy import pprint
from sympy.abc import A, B, C
from sympy.logic.boolalg import And, Not, Or
from sympy.logic.boolalg import to_cnf

'''
Tabela 1
A B C a 
V V V b  -- ABC  
V V F c  -- ABC'
V F V d  -- AB'C
V F F e  -- AB'C'
F V V f  -- A'BC
F V F g  -- A'BC'
F F V h  -- A'B'C
F F F i  -- A'B'C'
'''


    # Adquire a expressão booleana de acordo com a Tab. 1s
def extract_boolean_expression(truth_table: str):
    a = (A & B & C)                   if truth_table[0] == '1' else False
    b = (A & B & Not(C))              if truth_table[1] == '1' else False
    c = (A & Not(B) & C)              if truth_table[2] == '1' else False
    d = (A & Not(B) & C)              if truth_table[3] == '1' else False
    e = (Not(A) & B & C)              if truth_table[4] == '1' else False
    f = (Not(A) & B & Not(C))         if truth_table[5] == '1' else False
    g = (Not(A) & Not(B) & C)         if truth_table[6] == '1' else False
    h = (Not(A) & Not(B) & Not(C))    if truth_table[7] == '1' else False
    return(a | b | c | d | e | f | g | h)

if __name__ == '__main__':
    while(True):
        truth_table = input("Digite os oito bits relativos à tabela-verdade da expressão: ")
        for i in truth_table:
            if (i != '0' and i != '1'):
                print("Erro: O texto dado deve ser composto somente de 0s e 1s")
                continue
        if len(truth_table) != 8:
            print("Erro: A string dada tem " + str(len(truth_table)) + " caracteres, onde o esperado são 8")
            continue
        break
    expr = extract_boolean_expression(truth_table)
    cnf = to_cnf(expr)
    print("A tabela dada corresponde à seguinte expressão:")
    pprint(expr)
    print('\n')
    print("Em forma normal conjuntiva, a expressão corresponde a:")
    pprint(cnf)
    
    strcnf = str(cnf)
    
    pprint(cnf)
    
    