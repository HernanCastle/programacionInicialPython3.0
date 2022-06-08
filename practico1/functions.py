def sumar(a,b,c): #3 parámetros de entrada
    print( "El resultado de la suma es:",a + b + c)

def restar(a,b): #necesita 2 parámetros de entrada
    print( "El resultado de la resta es:", a - b)

def producto(a,b,c,d): # necesita 4 parámetros de entrada
    print( "El resultado de la producto es:", a * b * c * d)

'''
Realizamos los inputs para cargar en variables los valores (en la consola) 
necesarios para ejecutar las funciones que querramos
''' 
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese un número: "))
num3 = int(input("Ingrese un número: "))
num4 = int(input("Ingrese un número: ")) 

producto(num1,num2,num3,num4)


