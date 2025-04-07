# Trabajo práctico - Estructuras repetitivas. 

import random

#* 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea

for i in range(101):
    print(i)


#* 2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
#* ya que estamos manipulando nuestro ingreso de usuario como un elemento iterable, podremos preguntar if el primer caracter de user es igual a "-". Si es negativo no queremos que tome ese signo como otro digito, con lo cual, se lo vamos a extraer. 

user = str(input("Dime un número: "))

if user[0] == "-":
    user = user[1:]

digitos = len(user)

if digitos == 1:
    print("El número que has elegido tiene 1 solo digito.")
else:
    print("El número que has elegido tiene:", digitos, "digitos.")


#* 3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
#* Me tope con un pequeño inconveniente a la hora de llevar a cabo este ejercicio. Lo había resuelto muy simple pero noté que si el primer número ingresado era mayor, estaba en un problema, asique con un pequeño condicional le sumo 1 al valor que sea menor para excluir el mismo

suma = 0

num1 = int(input("Dime el primer número: "))
num2 = int(input("Dime el segundo número: "))

if num1 < num2:
    for i in range(num1 + 1, num2):
        suma += i
else:
    for i in range(num2 + 1, num1):
        suma += i

print("La suma de todos los números comprendidos entre los que has elegido es:", suma)


#* 4) Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0.

suma = 0

while True:
    user = int(input("Ingresa los valores de los productos para ir sumándolos - coloca 0 para terminar: "))

    if user == 0:
        break


    suma = suma + user
    print("Total a pagar:", suma)


#* 5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número.

numMisterioso = random.randint(0, 9)

numIntentos = 0

while True:
    user = int(input("Adivina el número entre el 0 y el 9. Buena suerte !!: "))
    numIntentos = numIntentos + 1

    if numMisterioso == user:
        print("¡Felicidades! El número era", numMisterioso, "y lo lograste en", numIntentos, "intentos.")
        break
    else:
        print("Vamos, no te desanimes. La próxima lo tienes.")


#* 6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

# Lo podemos hacer con un condicional que evalúe si es par...
for i in range(100, -1, -1):
    if i % 2 == 0:
        print(i)
    
# O directamente que retroceda de 2 en 2:
for i in range(100, -1, -2):
    print(i)


#* 7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

user = int(input("Dime un número positivo: "))
acum = 0

if user < 0:
    print("El número ingresado debe ser positivo.")
else:
    for i in range(0, user + 1):
        acum = acum + i

    print("La suma de todos los números entre 0 y", user, "es:", acum)


#* 8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

# acumuladores:
pares = 0
impares = 0
positivo = 0
negativo = 0


# Para probar el código basta con cambiar range(10) por range(100)...
for i in range(10):
    user = int(input("Ingresa un número: "))

    # Contar pares e impares:
    if user % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1

    # Contar positivos y negativos:
    if user > 0:
        positivo = positivo + 1
    elif user < 0:
        negativo = negativo + 1

print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)
print("Cantidad de números positivos:", positivo)
print("Cantidad de números negativos:", negativo)


#* 9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor).

#* Decidí usar un bucle for para controlar la cantidad de números a ingresar. Sumo todos los valores en una variable acumuladora y luego saco la media dividiendo por la cantidad. ¡Listo el pollo!

total = 0
cantidad = 10  # Para probar el código basta con cambiar el valor de esta variable por 100

for i in range(cantidad):
    numero = int(input("Ingresa un número: "))
    total = total + numero

media = total / cantidad

print("La media de los", cantidad, "números ingresados es:", media)


#* 10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

#* Probé usar slicing pero me costaba leerlo, así que usé reversed() con join para invertir los dígitos de forma más clara.
#* También me aseguré de que si el número es negativo, el signo quede adelante.

numero = input("Ingresa un número: ")

if numero.startswith("-"):
    invertido = "-" + ''.join(reversed(numero[1:]))
else:
    invertido = ''.join(reversed(numero))

print("El número invertido es:", invertido)
