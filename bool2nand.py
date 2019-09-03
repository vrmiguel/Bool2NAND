# -*- coding: utf-8 -*-
"""
github.com/vrmiguel/Bool2NAND
Ternary boolean expression into NANDs
TODO: Verificar se convert_ors_to_nand nunca trabalhará com uma expressão
com len != 3.
"""


import re
from sympy import pprint
from sympy.abc import A, B, C
from sympy.logic.boolalg import And, Not, Or, to_cnf

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


    # Adquire a expressão booleana de acordo com a Tabela 1
    # Exemplo: Uma entrada "10000000" teria saída (A & B & C)
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

    ''' 
        Converte ORs em NAND
        Parte do princípio de que or(a, b) = ((a⊼a)⊼(b⊼b)) '''
def convert_ors_to_nand(subexpr: str):
    if(len(subexpr) != 3):
        print("Erro fatal em convert_ors_to_nand()")
        exit(0)
    else:
        expr1 = '(' + subexpr[0] + " ⊼ " + subexpr[0] + ')'  # expr = (a⊼a)
        expr2 = '(' + subexpr[2] + " ⊼ " + subexpr[2] + ')'  # expr = (b⊼b)
        return '(' + expr1 + " ⊼ " + expr2 + ')'
    
    

    ''' Identifica se NOTs estão na expressão e tenta os converter para NANDs
        Parte do princípio de que not(x) = nand(x,x) ''' 
def convert_nots_to_nand(subexpr:str):    
    if(subexpr[0] == '~'):
        expr = '(' + subexpr[1] + '⊼' + subexpr[1] + ')'
        subexpr.pop(0)
        subexpr.pop(0)
        subexpr.insert(0, expr)
        
    try:
        z = subexpr.index('~')
    except ValueError:  # Caso não exista outro NOT na string
        return subexpr
    else:       # Caso exista outra, converta-a em NANDs
        expr = '(' + subexpr[z+1] + '⊼' + subexpr[z+1] + ')'
        subexpr.pop(z)
        subexpr.pop(z)
        subexpr.insert(z, expr)
        return(subexpr)
    
    # Converte subtermos da expressão em uma lista. Ex.: "A | B | C" -> ['A', '|', 'B', '|', 'C']
def get_terms(subexpr: str):
    subexpr = re.findall(".|.", subexpr)          #Obtém todos os termos entre OR  
    return([x for x in subexpr if x != ' ' and x != '(' and x != ')']) # Filtra espaços e parênteses 

    # Converte a expressão em FNC em uma expressão de NANDs 
def convert_to_nand(cnf: str):
    splitcnf = cnf.split("&") # Divide a string de forma normal conjuntiva em substrings somente com operações OR
    splitcnf = [x.strip() for x in splitcnf] # Remove espaços no começo e fim de cada substring
    terms_list = [get_terms(x) for x in splitcnf]
    print('Original em termos: ', terms_list)
    terms_list = [convert_nots_to_nand(x) for x in terms_list]
    print('NOTs convertidas: ', terms_list)
    terms_list = [convert_ors_to_nand(x) for x in terms_list]
    print('ORs convertidas: ', terms_list)
    
    #print(terms_list)    

if __name__ == '__main__':
        # Loop lê string de tabela-verdade enquanto o input for incorreto
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
    
    expr = extract_boolean_expression(truth_table) # Extrai expressão booleana da tabela-verdade
    cnf = to_cnf(expr, simplify=True) # e a converte para a forma normal conjuntiva em seus termos mais simples
    
    '''
    print("A tabela dada corresponde à seguinte expressão:")
    pprint(expr)
    print('\n')
    print("Em forma normal conjuntiva, a expressão corresponde a:")
    pprint(cnf)
    '''
    convert_to_nand(str(cnf)) # Transforma a forma normal conjuntiva em string    