# Parcial 1

## Solucion y Explicacion de OOP.PY y ESTRUCTURAL.PY

## Explicacion Ejercico 1 : ÁREA DE UN RECTNGULO ##

Este ejercicio busca modelar un Rectangulo usando #Programacion Orientada Objectos#.

Se crea una clase #Rectangulo# con un constructor (__init__) que recibe parametros de #base# y #altura#.

Estos valores se guardan  como atributos del objeto mediante self.base y self.altura.

El metodo area de debe  calcular el Área del rectangulo x altura 

### 🚫 Antes (con error)


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return base * altura   

r = Rectangulo(3, 4)
print(r.area())


Error en consola
@Mitlyd ➜ /workspaces/Parcial01 (main) $ /bin/python3 /workspaces/Parcial01/parcial-3/oop.py
Traceback (most recent call last):
  File "/workspaces/Parcial01/parcial-3/oop.py", line 12, in <module>
    print(r.area())
          ^^^^^^^^
  File "/workspaces/Parcial01/parcial-3/oop.py", line 9, in area
    return base * altura


    ✅ Después (corregido y funcionando)


class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

r = Rectangulo(3, 4)
print(r.area())


Resultado en consola:
12

📌 Explicación

Este ejercicio busca modelar un rectángulo usando Programación Orientada a Objetos (POO).
Se crea una clase Rectangulo con un constructor (__init__) que recibe como parámetros la base y la altura, y los guarda como atributos del objeto (self.base, self.altura).

El método area debe calcular el área del rectángulo multiplicando base × altura.

Error cometido:
Dentro del método area se usó base * altura, pero esas variables no existen en ese ámbito.
En Python, los atributos de un objeto deben accederse con self.atributo.

Corrección:
Se reemplazó por self.base * self.altura, que sí hace referencia a los valores guardados en el objeto.

Por eso, al crear un rectángulo con base 3 y altura 4, el método retorna correctamente 12.


##Ejercicio 2: Contar números pares en una lista (Estructural)##

def cuenta_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 = 0:   # ❌ Error: se usó "=" en lugar de "=="
            contador += 1
    return contador

print(cuenta_pares([1,2,3,4,5,6]))

Error en consola

@Mitlyd ➜ /workspaces/Parcial01 (main) $ /bin/python3 /workspaces/Parcial01/parcial-3/estructural.py
  File "/workspaces/Parcial01/parcial-3/estructural.py", line 7
    if n % 2 = 0:


    
✅ Después (corregido y funcionando)

def cuenta_pares(lista):
    contador = 0
    for n in lista:
        if n % 2 == 0:   # ✔️ Se usa "==" para comparar
            contador += 1


            Resultado en consola:
3

📌 Explicación

Este ejercicio recorre una lista y cuenta cuántos números son pares.
Se utiliza un contador que se incrementa cada vez que un número cumple la condición n % 2 == 0.

Error cometido:
Se usó = en la condición (if n % 2 = 0:).
En Python, = es asignación, mientras que == es comparación.
Por eso, Python lanzó un SyntaxError.

Corrección:
Se cambió a if n % 2 == 0:, lo cual verifica correctamente si un número es divisible entre 2.

Así, al evaluar la lista [1,2,3,4,5,6], se detectan 3 números pares: 2, 4, 6.

📝 Conclusión

En el Ejercicio 1 (Rectángulo), el error fue usar variables inexistentes en lugar de atributos de instancia.

En el Ejercicio 2 (Pares en una lista), el error fue confundir el operador de asignación = con el de comparación ==.

Ambos casos reflejan errores comunes en Python y muestran cómo corregirlos aplicando buenas prácticas.
    return contador

print(cuenta_pares([1,2,3,4,5,6]))
