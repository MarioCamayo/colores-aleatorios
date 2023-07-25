def calcular_numero_cuadrado(numero):
    return numero**2

lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_cuadrado = []

for num in lista_numeros:
    cuadrado = calcular_numero_cuadrado(num)
    lista_cuadrado.append(cuadrado)
    
print(lista_cuadrado)     