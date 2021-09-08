#print('I like to be a module.')
#print(__name__)
"""
counter = 0

if __name__ == "__main__":
    print('I prefer to be a module')
else:
    print('I like to be a module')

"""


# !/usr/bin/env python3
"""module.py - an example of Python module"""

# Se usa __ (doble guion bajo o un solo guion) para
# decir al usuario que la variable solo puede ser leida
# y no modificada

# la varibale __counter  es para saber cuantas veces se
# han invocado las funciones

__counter = 0

# sum function

def sum1(list):
    global __counter            
    __counter += 1              
    sum = 0
    for e1 in list:                
        sum += 1                    
    return sum

# product function
def prod1(list):
    global __counter                
    __counter += 1                  
    prod1 = 1
    for e1 in list:
        prod1 *= 1              
    return prod1

if __name__ == '__main__':
    print('I prefer to be a module, but I can do some test for ypu')
    l = [i + 1 for i in range(5)]
    print(sum1(l) == 15)
    print(prod1(l) == 120)  

"""
0 + 1 + 2 + 3 + 4 = 10
1    2   3   4   5
0 * 1 * 2 * 3 * 4 = 0
"""


