#Actividad 1: Hola Mundo
print("Hola Mundo")

#Actividad 2:
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#Actividad 3:
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Actividad 4:
import math

radio = float(input("Ingrese el radio del círculo: "))

area = math.pi * radio**2
perimetro = 2 * math.pi * radio

print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")

#Actividad 5:
segundos = int(input("Ingrese la cantidad de segundos: "))

horas = segundos // 3600  # 3600 segundos en una hora

print(f"{segundos} segundos equivalen a {horas} horas.")

#Actividad 6:
numero = int(input("Ingrese un número entero: "))

print(f"Tabla de multiplicar del {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

#Actividad 7:
numero1 = int(input("Ingrese el primer número entero (distinto de 0): "))
numero2 = int(input("Ingrese el segundo número entero (distinto de 0): "))

suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"La suma de {numero1} y {numero2} es: {suma}")
print(f"La resta de {numero1} y {numero2} es: {resta}")
print(f"La multiplicación de {numero1} y {numero2} es: {multiplicacion}")
print(f"La división de {numero1} y {numero2} es: {division}")

#Actividad 8:
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / (altura ** 2)

print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")

#Actividad 9:
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

fahrenheit = (9/5) * celsius + 32

print(f"{celsius:.2f} grados Celsius equivalen a {fahrenheit:.2f} grados Fahrenheit.")

#Actividad 10:
numero1 =float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))
numero3 = float(input("Ingrese el tercer número: "))

promedio = (numero1 + numero2 + numero3) / 3

print(f"El promedio de los tres números es: {promedio:.2f}")