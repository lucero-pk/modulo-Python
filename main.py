from module import sum1, prod1
#print(module.counter)

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(sum1(zeroes))
print(prod1(ones))

"""
0 + 1 + 2 + 3 + 4 = 10

1    2   3   4   5

0 * 1 * 2 * 3 * 4 = 0

=============================
result sum
e1 = 0 + 1 + 2 + 3 + 4
sum = 1, 2, 3, 4, 5

result product
e1 = 1 * 2 * 3 * 4 * 5
prod1 = 1, 1, 1, 1, 1
=============================
"""
print('\n ================')

nombre = 'lu'

lista = [1, 2, 3, 4, 5]
sum = 0
for i in lista:
    #print(i)
    sum += i
print(f'la suma de los elementos de la lista es {sum}')

# fomas de concatenar e imprimir un mensaje en python
print(f"Hola {nombre}")
print("Hola, {}".format(nombre))
print('Hola ' + nombre)
print('Hola', nombre)