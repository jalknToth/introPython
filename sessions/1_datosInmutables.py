# Datos inmutables en Python (mutable data)
print('='*9,'D A T O S  I N M U T A B L E S','='*9)
print("'"*50,'\n') #\n: (next line)

# Los datos inmutables NO se pueden modificar después de su creación. 
# Cualquier operación que parezca modificarlos, en realidad crea una nueva instancia.
"""
En Python, entender la diferencia entre variables, objetos y valores es crucial para programar eficazmente.
Cada objeto en Python tiene un 'tipo' que define qué tipo de datos puede almacenar y qué operaciones se pueden realizar con él.
Un objeto es una 'entidad' que contiene 'datos' (atributos) y 'código' para manipular esos datos (métodos). 
Los objetos son como contenedores con datos y acciones. Todo en Python es un objeto, incluso las clases.
Los valores son la información dentro de esos contenedores.
Las variables son etiquetas que apuntan a esos contenedores. Una variable puede contener cualquier tipo de objeto.
"""
# 1. Enteros (int) (integer)
a = 9
print('='*18,'E N T E R O S','='*18,)
print("'"*50)
print("Valor de a es", a)

# Intentar modificar 'a' (modify 'a')
# Asignar un nuevo valor de 'a' con un operador de asignacion (+=) (assign a mew value for a with an assignment operator)
a += 2  # Equivalente a = a + 2 (equal a = a + 2)
print("Valor de a después de 'a += 2' es", a) 
print("Este tipo de dato es", type(a))
print("-" * 20)

# 2. Flotantes o decimales (float)
b = 3.2
print("\n=== Flotantes ===")
print("Valor de b es", b)
print("Este tipo de dato es", type(b))
print("-" * 20)

# 3. Cadenas (str) - texto entre '' o ""
c = 'Hola'
print("\n=== Cadenas ===")
print("Valor de c es", c)
print("Este tipo de dato es", type(c))

# Intentar modificar 'c'
c +=  " Mundo" # Equivalente a c = c + " Mundo"
print("Valor de c después de 'c += \" Mundo\"'es", c)

# 4. Booleanos (bool)
d = True
e = False
print("\n=== Booleanos ===")
print("\nValor de d es", d)
print("Valor de e es", e)
print("Estos tipos de dato son", type(d))
print("-" * 20)

# 5. Tuplas (tuple) - mantienen el orden, son inmutables
f = ('amarillo', 'azul', 'rojo')
print("\n=== Tuplas ===")
print("Valor de f es", f)
print("Este tipo de dato es", type(f))
print("-" * 20)
# Intentar modificar una tupla (generará un error)
# f[0] = 'verde'  # Descomenta esta línea para ver el error

# 6. Rangos (range) son secuencias inmutables de números
g = range(9) # (secuencia del 0 al 8)
print("\n=== Rangos ===")
print("Valor de g es", g)
print("Los valores de g son", list(g)) #list convierte el rango en lista
print("Este tipo de dato es", type(g))
print("-" * 20)

# 7. Conjuntos congelados (frozenset) - Inmutables, no se pueden añadir o eliminar elementos
print("\n=== Conjuntos congelados ===")
h = frozenset({'amarillo', 'azul', 'rojo'})
print("Valor de h es", h)
print("Este tipo de dato es", type(h))
print("-" * 20)

print("\nEjercicios", "="*19)

print("-" * 30)
print("\nEjercicio 1: Crea Nuevas Variables")
# Crea nuevas variables con diferentes tipos de datos(int.float,str...)
# Imprime el valor de cada variable.
print("-" * 30)
print("\nEjercicio 2: Tipos de Datos")
# 3. Imprime el tipo de dato de cada variable usando type(). 
# 4. Comenta todo lo que quieras memorizar con # o doble linea con"""
print("-" * 30)