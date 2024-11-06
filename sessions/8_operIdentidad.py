# Operadores de identidad
print("\n===== O P E R A D O R E S  D E  I D E N T I D A D =====")
print("===== is ================================= is not =====")
print("'" * 55)
print("Se utilizan para comparar si dos variables se""\nrefieren al mismo objeto en la memoria.")
print("-" * 55)
print("* 'is' devuelve 'True' si las variables apuntan al""\nmismo objeto en memoria. 'False' en caso contrario.")
print("-" * 55)
print("* 'is not' devuelve 'True' si las variables no apuntan""\nal mismo objeto en memoria. 'False' en caso contrario.")
print("-" * 55)
print("La comparación de identidad 'is' es diferente de la""\ncomparación de igualdad '=='.")
print("-" * 55)
print("Dos variables pueden ser iguales en valor '=='""\npero no idénticas 'is'")
print("-" * 55)
print("* Python genera dos objetos diferentes en memoria""\npara los datos mutables")
print("-" * 55)
print("* Python optimiza la memoria reutilizando las mismas""\n instancias para los datos inmutables")
print("-" * 55)

print("\n==================== E J E M P L O ====================")
print("'" * 55)
print('Comparemos la identidad de tres objetos: ')
# crear tres variables x,y,z
x = [1,2,3]
y = x
z = [1,2,3]
# imprime las variables
print("x =",x ,"   |   y =",y ,"   |   z =",z)
# verifica si las variables son identicas
print("\n..........'x' y 'y' son el mismo objeto:", x is y)
print("..........'x' y 'y' tienen el mismo valor:", x == y)
print("..........'x' y 'z' son distintos objetos: ", x is not z)
print("..........'x' y 'z' tienen el mismo valor: ", x == z)
print("..........'z' y 'y' son distintos objetos: ", z is not y)
print("..........'y' y 'z' son distintos objetos:", y is not z)
print("..........'y' y 'z' tienen el mismo valor:", y == z)
print("-" * 55)

print("\n================= E J E R C I C I O S =================")
print("'" * 55)
# Ejercicio 1
print("Ejercicio 1. Compara la identidad de datos inmutables""\n(str, int, float, bool, range, tuple, frozenset)")
# crear tres variables a,b,c. (str, int, float, bool, range, tuple, frozenset)")
a = "auditor"
b = a
c = "auditor"
# verifica si las variables son identicas
print("\na = 'auditor'    |       b = a      |     c = 'auditor'")
# Imprime si 'a' y 'b' son el mismo objeto."
print("\n..........'a' y 'b' son el mismo objeto:", a is b)
# Imprime si 'a' y 'c' son el mismo objeto."
print("..........'a' y 'c' son el mismo objeto:", a is c)
# Imprime si 'c' y 'b' son el mismo objeto."
print("..........'c' y 'b' son el mismo objeto:", c is b)
# Imprime si 'b' y 'c' son el mismo objeto."
print("..........'b' y 'c' son el mismo objeto:", b is c)
# imprime las variables
print("\na:",a, "           b:", b, "          c:", c)
print("-" * 55)

# Ejercicio 2
print("'" * 55)
print("Ejercicio 2. Compara la identidad  de datos mutables""\n(list, dict, set)")
# crear tres variables a,b,c. (list, dict, set)")
set1 = {1,2,3}
set2 = set1
set3 = {1,2,3}
# verifica si las variables son identicas
print("\na = 'auditor'    |       b = a      |     c = 'auditor'")
# Imprime si 'a' y 'b' son el mismo objeto."
print("\n..........'a' y 'b' son el mismo objeto:", a is b)
# Imprime si 'a' y 'c' son el mismo objeto."
print("..........'a' y 'c' son el mismo objeto:", a is c)
# Imprime si 'c' y 'b' son el mismo objeto."
print("..........'c' y 'b' son el mismo objeto:", c is b)
# Imprime si 'b' y 'c' son el mismo objeto."
print("..........'b' y 'c' son el mismo objeto:", b is c)
# imprime las variables
print("\na:",a, "           b:", b, "          c:", c)
print("-" * 55)

# Ejercicio 3
print("'" * 55)
print("Ejercicio 3. Compara datos mutables con inmutables")
# Crear una lista, un diccionario y un conjunto.
# Crear nuevas variables que apunten a los mismos objetos.
# Crear nuevas variables con los mismos valores pero diferentes objetos.

# Imprimir los resultados de las comparaciones de identidad de las listas.
print("\nComparaciones de identidad para listas:")
print("\nComparaciones de identidad para diccionarios:")
print("\nComparaciones de identidad para conjuntos:")
print("-" * 55)