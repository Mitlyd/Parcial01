#AI-TRAP:ESTRUCTURAL

def cuenta_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 == 0:
            contador += 1
    return contador

print(cuenta_pares([1,2,3,4,5,6]))
