# Operadores de pertenencia
print("\n=== O P E R A D O R E S  D E  P E R T E N E N C I A ===")
print("=== in ===================================== not in ===")
print("'" * 55)
print("Se utilizan para verificar si un valor o""\nsecuencia se encuentra dentro de otra secuencia.")
print("*'in' devuelve 'True' si el valor especificado""\nse encuentra dentro de la secuencia.")
print("*'not in' devuelve 'True' si el valor especificado""\nno se encuentra dentro de la secuencia.")
print("-" * 55)

print("\n=================== E J E M P L O S ===================")
print("'" * 55)
"""
# Pedir al usuario cinco numeros separados por esapcio del 1 al 40
x = input("Ejemplo 1. Ingresa cinco números separados por espacios""\ndel 1 al 40: ")
# Separar la entrada en una lista de strings
z = x.split()
print(z)
# Convertir la lista de strings a una lista de enteros
w = [int(numero) for numero in z]
print(w)
# Verificar si un número está presente en la lista
print("El 23 esta en la lista:", 23 in w)
print("El 16 esta en la lista:", 16 in w)
# Verificar si un número no está en la lista
print("El 11 no esta en la lista:", 11 not in w)
print("El 38 no esta en la lista:", 38 not in w)
print("-" * 55)

#preguntar al usuario por una palabra
y = str.lower(input("Ejemplo 2. Escribe una palabra: "))
#verificar si un numero esta en la palabra
print("'p' esta en la palabra","p" in y)
print("'y' esta en la palabra","y" in y)
print("'t' esta en la palabra","t" in y)
print("'h' no esta en la palabra","h" not in y)
print("'o' no esta en la palabra","o" not in y)
print("'n' no esta en la palabra","n" not in y)
print("-" * 55)
"""
print("\n================= E J E R C I C I O S =================")
print("'" * 55)
# Ejercicio 1
print("\nEjercicio 1")
# Define una lista de colores
colores = ["rojo", "azul"]
# Pide al usuario que ingrese un color
color = input("Ingresa un color de la bandera de Haiti: ")
# Imprime si el color está en la lista o no usando operadores de pertenencia
print("el color '", color, "' esta en la bandera de Haití: ", color in colores)

# Ejercicio 2
print("-" * 40)
print("\nEjercicio 2")
# Define una tupla de vocales
vocales = ("a", "e", "i", "o", "u")
# Pide al usuario que ingrese una letra
letra = input("Ingresa una letra: ").lower()
# Imprime si la letra es una vocal o no usando operadores de pertenencia
print("la letra '", letra, "' es una vocal: ", letra in vocales)

# Ejercicio 3
print("-" * 40)
print("\nEjercicio 3")
# Define una cadena de texto
texto = str(input('Ingresa un texto: '))
# Pide al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")
# Imprime si la palabra está presente en el texto o no usando 
print("la palabra '", palabra, "' esta en el texto: ", palabra in texto)
print("-" * 40)

