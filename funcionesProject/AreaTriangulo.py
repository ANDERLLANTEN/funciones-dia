# ejemplo para calcular el area de un triangulo

#variables de entrada
base =int( input("ingrese la base: "))
altura=int( input("ingrese la altura: "))

#proceso
def calcularAreaTriangulo(b,a):
    area = (b*a)/2
    return  area

#invocar la funcion
resultado = calcularAreaTriangulo(base,altura)

#salida
print(f"el area del triangulo cuya base {base } y altura {altura} es: {resultado}")

#funcion con argumentos  predeterminados
def  my_function(country  = "colombia"):
    print("I am from "+country)

#invocar la funcion
my_function()
my_function("sweden")
my_function("francia")
my_function("brazil")

#argumentos arbitrarios
def mostrarEstudiantes(*args):
    print("el estudiantes: "+args[2])

#invocamos la funcion
mostrarEstudiantes( "email", "tobias", "linus")

def mostrarCarros(carro1, carro2, carro3):
    print("el carro es: "+carro2)
mostrarCarros(carro1 = "BMW", carro3= "ferrari", carro2= "ford")

def mostrarClientes(**kwargs):
    print("su apellido es: "+kwargs["apellido"])
mostrarClientes(nombre = "tobias", apellido = "Refsnes")

def mifuncion():
    pass

#ejemplo funciones integradas

x = min (5, 10, 25)
y = max (5, 10, 25)

print(x)
print(y)

num1 = pow(7, 4)

print(num1)


#modulo de matematicas
import math

num2 = math.sqrt(34)

print(num2)


# ceil y floor

import math
num3 = math.ceil(7.8)
num4 = math.floor(7.8)

print(num3)  # returns 8
print(num4)  # returns 7
