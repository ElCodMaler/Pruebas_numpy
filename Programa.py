import numpy as np
"""
Para crear una funcion con su respectivo tamaño
se usa la funcion de numpy 'poly1d' que recibe
como parametro un array de una dimencion, en 
donde se le podra crear la cantidad de numeros
que se deseen crear, y dependiendo de la cantidad de
posiciones que ocupen cada valor del array, definira
una funcion del tamaño que tenga los valores del array
"""
#funcion crear funcion
def crearFuncion(matriz):
    while True:
        valor = input('Escriba un numero: ')  
        if(valor == ''):
            break
        else:
            matriz.append(int(valor))
    return matriz
#inicializacion de variables
M = []
#entrada de datos
M = crearFuncion(M)
# definiendo una funcion polinominal
func = np.poly1d(M)
print("Polynomial function:\n", func)
  
# calculating the derivative
derivative = func.deriv()
print("Derivative, f(x)'=\n", derivative)
  
# # calculates the derivative of after 
# # given value of x
# print("When x=2  f(x)'=", derivative(0.2))