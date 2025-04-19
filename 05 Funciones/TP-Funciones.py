# Práctico 2: Funciones en Python
#* 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def imprimir_hola_mundo():
    print("Hola Mundo!")

imprimir_hola_mundo() 


#* 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario.

nombre = input("Como es tu nombre: ")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

saludar_usuario(nombre)


#* 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

nombre = input("Dime tu nombre: ")
apellido = input("Dime tu apellido: ")
edad = int(input("Ahora dime cuantos años tienes: "))
residencia = input("Por último, cuentanos de donde eres: ")

def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

informacion_personal(nombre, apellido, edad, residencia)


#* 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

pi = 3.1415

def calcular_area_circulo(radio):
    area = pi * radio ** 2
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * pi * radio
    return perimetro

num = float(input("Dime el radio: "))

area = calcular_area_circulo(num)
perimetro = calcular_perimetro_circulo(num)

print(f"El área del círculo cuyo radio es {num} es: {area}")
print(f"El perímetro del círculo cuyo radio es {num} es: {perimetro}")


#* 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def segundos_a_horas(segundos):
    horas = segundos / 3600 
    return horas

segundos = int(input("Dime una cantidad de segundos: "))

horas = segundos_a_horas(segundos)

print(f"La cantidad de horas que hay en {segundos} segundos es: {horas}")


#* 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def tabla_multiplicar(numero):
    for i in range(1, 11): 
        print(f"{numero} * {i} = {numero * i}")

numero = int(input("Dime un número y te diré la tabla de multiplicar de dicho número: "))

tabla_multiplicar(numero)


#* 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # hacemos un condicional preguntando que todo se va a dividir siempre y cuando la variable b sea distinta de cero. 
    if b != 0:
        division = a / b
    else:
        division = "Error: División por cero"
    return (suma, resta, multiplicacion, division)

a = float(input("Dime el primer número: "))
b = float(input("Dime el segundo número: "))

resultados = operaciones_basicas(a, b)

print(f"Los resultados de las operaciones son:")
print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
print(f"División: {resultados[3]}")


#* 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Dime tu peso en kilogramos: "))
altura = float(input("Dime tu altura en metros: "))

imc = calcular_imc(peso, altura)

print(f"Tu índice de masa corporal (IMC) es: {imc:.2f}")


#* 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def celsius_a_fahrenheit(celsius):
    # 1 celsius == 33,8 fahrenheit
    conver = (celsius * 9 / 5) + 32
    return conver

temp = float(input("Dime una temperatura en grados Celsius y te diré su equivalente en grados Fahrenheit: "))

print(celsius_a_fahrenheit(temp))


#* 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3

    return promedio

num1 = float(input("Dime la primer calificación: "))
num2 = float(input("Dime la segunda calificación: "))
num3 = float(input("Dime la tercer calificación: "))

resultado = calcular_promedio(num1, num2, num3)

print(f"El promedio de {num1}, {num2}, {num3} es: {resultado}.")