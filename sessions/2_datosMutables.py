import pandas

# Datos mutables en Python
# Para usar pandas se debe instalar el ambiente: python -m venv [name]
# luego activar el ambiente: source [name]/bin/activate
# instala pandas: pip install pandas

# Los datos mutables se pueden modificar después de su creación. 
# Esto significa que podemos agregar, eliminar o cambiar elementos dentro de ellos.

#1. Listas:
# - Mantienen el orden en que se agregaron los elementos.
# - Pueden contener diferentes tipos de datos.

print("\n=== listas ===")
x = ['amarillo', 'azul', 'rojo']
print("Este tipo de dato es", type(x))
print("Estos son sus elementos:", x)

# Modificar un elemento de la lista:
x[1] = 'verde'
print("Modificada es:", x)

# Agregar un elemento al final:
x.append('blanco')
print("Agregamos color blanco:", x)

# Eliminar un elemento específico:
x.remove('rojo')
print("Eliminamos rojo:", x)

print("-" * 20)

#2. Diccionarios:
# - Almacenan pares clave-valor.
# - Las claves deben ser únicas e inmutables (como cadenas o números).
# - Se puede acceder a los valores a través de sus claves.

print("\n=== Diccionarios ===")
carro = {"marca": "Honda","modelo": 2000}
carros = {"marca": {"Honda","Toyota"},"modelo": {2000,2004}}

print("Este tipo de dato es", type(carro))
print("Este tipo de dato es", type(carros))
print("Estos son sus elementos", carro)
print("Estos son sus elementos", carros)
# Modificar el valor asociado a una clave:
carro['modelo'] = 2002
print("Modificamos el modelo", carro)

# Agregar un nuevo par clave-valor:
carro['color'] = 'Azul'
print("Agregamos el color", carro)

# Eliminar un par clave-valor:
del carro['modelo']
print("Eliminamos el modelo", carro)

print("-" * 20)

# convertir Dict en tabla de datos
# tabla = pandas.DataFrame(carro)

#3. Conjuntos (sets):
# - Almacenan elementos únicos sin un orden definido.
# - Son mutables, pero solo se pueden agregar o eliminar elementos, no modificarlos directamente.

print("\n=== Conjuntos ===")
y = {'amarillo', 'azul', 'rojo'}
print("Este tipo de dato es", type(y))
print("Estos son sus elementos", y)

# Agregar un elemento al conjunto:
y.add('verde')
print("Agregamos verde", y)

# Eliminar un elemento del conjunto:
y.remove('amarillo')
print("Eliminamos amarillo", y)

print("\nEjercicios", "="*19)

print("-" * 30)
print("\nEjercicio 1: Crear lista")
# Crea una lista con diferentes de datos(str,int,float..)
# Imprime la lista en la consola

print("-" * 30)
print("\nEjercicio 2: Crear Diccionario")
# Crea un diccionario de 10 palabras en ingles
# Imprime en la consola
print("-" * 30)
