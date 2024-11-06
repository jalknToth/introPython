# Operadores Logicos
print("\n== O P E R A D O R E S  L O G I C O S ==")
print("'" * 40)
print("Se utilizan para combinar sentencias" "\ncondicionales y evaluar su veracidad")
print("Son: 'and','or', 'not'")

print("-" * 40)

print("\n============ operador A N D ============")
print("'" * 40)
print("Devuelve 'True' si ambas expresiones" "\na sus lados son 'True'")
print("Devuelve 'False' en cualquier otro caso")
print("-" * 40)
#pregunta al usuario por un numero
x = int(input("Ej. Ingresa un numero "))
print("-" * 40)
#evalua con el operador 'and'
print(x,'es mayor que 2 Y menor que 10:', x > 2 and x < 10)
print(x,'es mayor que 10 Y menor que 20:', x > 10 and x < 20)
print("-" * 40)

print("\n============= operador O R =============")
print("'" * 40)
print("Devuelve 'True' si al menos una de" "\nlas expresiones a sus lados son 'True'")
print("Devuelve 'False' solo si ambas""\nexpresiones son 'False'")
print("-" * 40)
#evalua con el operador 'or'
print(x,'es mayor que 2 O menor que 10:', x > 2 or x < 10)
print(x,'es mayor que 10 O menor que 20:', x > 10 or x < 20)
print("-" * 40)

print("\n============ operador N O T ============")
print("'" * 40)
print("Invierte el valor de la verdad")
print("Devuelve 'True' si es 'False'")
print("Devuelve 'False' si es 'True'")
print("-" * 40)
# Evaluar con el operador 'not'
print(x, 'NO es mayor que 10:', not (x > 10))
print(x, 'NO es mayor que 20:', not (x > 20))
print("-" * 40)

print("\n========== E J E R C I C I O S ==========")
print("'" * 40)
"""
# Ejercicio 1: operador AND
print("\nEjercicio 1: operador == A N D ==")
print("-" * 40)
edad = int(input("Ingresa tu edad: "))
documento = input("¿Tienes licencia de conducir? (si/no): ")
# Verificar si la persona es mayor de edad (18 años o más) y tiene licencia
permiso = edad >= 18 and documento.lower() == "si"
print("¿Puede conducir?", permiso)
print("-" * 40)

# Ejercicio 2: operador OR
print("\nEjercicio 2: operador == O R ==")
print("-" * 40)
dia = input("Ingresa un día de la semana: ")
finSemana = dia.lower() == "sabado" or dia.lower() == "domingo"
print("¿Es fin de semana?", finSemana)
print("-" * 40)

# Ejercicio 3: operador NOT
print("\nEjercicio 3: operador == N O T ==")
print("-" * 40)
numero = int(input("Ingresa un número: "))
par = numero % 2 == 0
print("El número es impar:", not par)
print("-" * 40)
"""

