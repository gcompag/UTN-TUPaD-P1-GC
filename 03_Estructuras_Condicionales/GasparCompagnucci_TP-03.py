#Actividad 1

edad = int(input("Por favor, introduce tu edad: "))

if edad > 18:
    print("Es mayor de edad")

#Actividad 2

nota = float(input("Por favor, ingresa tu nota: "))

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#Actividad 3

while True:
  try:
    numero = int(input("Por favor, ingrese un número par: "))
    if numero % 2 == 0:
      print("Ha ingresado un número par")
      break  # Salimos del bucle si el número es par
    else:
      print("Por favor, ingrese un número par")
  except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")

#Actividad 4

edad_usuario = input("Ingrese su edad: ")
try:
    edad= int(edad_usuario)
    if edad <12:
        print("Niño/Niña")
    elif edad >= 12 and edad <18:
        print("Adolescente")
    elif edad >= 18 and edad <30:
        print("Adulto/a Joven")
    else:
        print("Adulto/a") 
except ValueError:
    print("Por favor, introduce un número entero válido para la edad")

#Actividad 5

def verificar_contrasena():
  contrasena = input("Ingrese su contraseña: ") #Se solicita al usuario que ingrese una contraseña
  longitud = len(contrasena)
  if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
  else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

# Ejecutamos la función para que el programa se ponga en marcha
verificar_contrasena()

#Actividad 6

import random
from statistics import mode, median, mean, StatisticsError

# Definir la lista de números aleatorios
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, mediana y media
try:
    moda = mode(numeros_aleatorios)
except StatisticsError:
    moda = "No hay una única moda"  # Manejar el caso de múltiples modas
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

# Determinar el sesgo
print(f"Lista de números aleatorios: {numeros_aleatorios}")
print(f"Moda: {moda}")
print(f"Mediana: {mediana}")
print(f"Media: {media}")

if isinstance(moda, (int, float)):
    if media > mediana > moda:
        print("La distribución tiene un sesgo positivo o a la derecha.")
    elif media < mediana < moda:
        print("La distribución tiene un sesgo negativo o a la izquierda.")
    elif media == mediana == moda:
        print("La distribución no tiene sesgo.")
    else:
        print("No se puede determinar el sesgo claramente según el criterio proporcionado.")
else:
    if media > mediana:
        print("La media es mayor que la mediana.")
    elif media < mediana:
        print("La media es menor que la mediana.")
    else:
        print("La media y la mediana son iguales.")
    print("No hay una única moda, por lo que la determinación del sesgo es menos precisa.")

#Actividad 7
# Solicitar una frase o palabra al usuario
texto = input("Ingresá una frase o palabra: ")

# Verificar si termina con una vocal (minúscula o mayúscula)
if texto[-1].lower() in "aeiou":
    texto += "!"

# Mostrar el resultado
print("Resultado:", texto)

#Actividad 8
# Solicitar el nombre al usuario
nombre = input("Ingresá tu nombre: ")

# Mostrar opciones
print("Elegí una opción:")
print("1. Mostrar el nombre en MAYÚSCULAS")
print("2. Mostrar el nombre en minúsculas")
print("3. Mostrar el nombre con la Primera Letra en mayúscula")

# Solicita la opción al usuario
opcion = input("Ingresá 1, 2 o 3: ")

# Transforma el nombre según la opción elegida
if opcion == "1":
    resultado = nombre.upper()
elif opcion == "2":
    resultado = nombre.lower()
elif opcion == "3":
    resultado = nombre.title()
else:
    resultado = "Opción no válida."

# Mostrar el resultado
print("Resultado:", resultado)

#Actividad 9
# Solicita al usuario la magnitud del terremoto
magnitud = float(input("Ingresá la magnitud del terremoto: "))

# Clasifica según la escala de Richter
if magnitud < 3:
    clasificacion = "Muy leve (imperceptible)."
elif 3 <= magnitud < 4:
    clasificacion = "Leve (ligeramente perceptible)."
elif 4 <= magnitud < 5:
    clasificacion = "Moderado (sentido por personas, pero generalmente no causa daños)."
elif 5 <= magnitud < 6:
    clasificacion = "Fuerte (puede causar daños en estructuras débiles)."
elif 6 <= magnitud < 7:
    clasificacion = "Muy Fuerte (puede causar daños significativos)."
else:
    clasificacion = "Extremo (puede causar graves daños a gran escala)."

# Mostrar el resultado
print(f"Clasificación: {clasificacion}")

#Actividad 10
# Solicitar datos al usuario
hemisferio = input("¿En qué hemisferio estás? (N/S): ").strip().upper()
dia = int(input("Ingresá el día (número): "))
mes = int(input("Ingresá el mes (número): "))

# Función para convertir fecha a un valor comparable (día del año)
def fecha_en_dia_del_anio(dia, mes):
    from datetime import date
    return (date(2024, mes, dia) - date(2024, 1, 1)).days + 1  # +1 porque el 1/1 es día 1

# Convertir la fecha a día del año
dia_del_anio = fecha_en_dia_del_anio(dia, mes)

# Definir los rangos en días del año para facilitar la comparación
# Nota: usamos año bisiesto para evitar errores con febrero
estaciones = {
    'N': {
        'Invierno':    [(355, 366), (1, 79)],
        'Primavera':   [(80, 171)],
        'Verano':      [(172, 264)],
        'Otoño':       [(265, 354)],
    },
    'S': {
        'Verano':      [(355, 366), (1, 79)],
        'Otoño':       [(80, 171)],
        'Invierno':    [(172, 264)],
        'Primavera':   [(265, 354)],
    }
}

# Determinar estación
estacion_actual = "Desconocida"
for estacion, rangos in estaciones[hemisferio].items():
    for inicio, fin in rangos:
        if inicio <= dia_del_anio <= fin:
            estacion_actual = estacion
            break

# Mostrar resultado
print(f"Estás en el hemisferio {hemisferio}. La estación del año es: {estacion_actual}.")

#Fin De Actividad




