'''
Escriba una función en Python que permita determinar si un número es perfecto o no. Un
número perfecto es un número entero positivo cuyo valor es igual a la suma de todos sus divisors
enteros positivos. (https://es.wikipedia.org/wiki/Número_perfecto)
'''

print("========================================")
print("=    Ejercicio No. 3, Tarea No. 2      =")
print("=       Por: Guillermo Mora B.         =")
print("========================================")

print("")

#Funcion para solicitar los numeros al usuario
def solicitar_numero():
    num_str1 = input("Digite el numero a verificar: ")

    return(num_str1)

#Funcion para convertir los string en integer
def convertir_numero(num1):
    num1 = int(num1)

    return(num1)

#Funcion para determinar si el numero es correcto
def verfifica_numero(num1):
    esta_correcto = False
    if num1 > 0:
        esta_correcto = True

    return (esta_correcto)

#Funacion pra realizar la busqueda de los divisores del numero
def busca_divisor(num1):
    maximo_rango = (num1 // 2) + 1
    resultado_division = 0
    #ciclo para comprobar divisores del numero
    for divisor in range(1,maximo_rango):
        if num1 % divisor == 0:
            resultado_division = resultado_division + divisor

    return(resultado_division)

#Funcion para vierificar si el numero es perfecto
def verifica_perfecto(num1,num2):
    numero_perfecto = False
    if num1 == num2:
        numero_perfecto = True

    return (numero_perfecto)

#Cuerpo del programa
salir = ""

while salir != "s" and salir != "S":
    numero_string = solicitar_numero()
    numero_int = convertir_numero(numero_string)
    numero_correcto = verfifica_numero(numero_int)

    if numero_correcto:
        suma_divisores  = busca_divisor(numero_int)
        numero_perfecto = verifica_perfecto(numero_int,suma_divisores)
        if numero_perfecto:
            print("El numero {} es un numero perfecto ".format(numero_int))
            print("")
        else:
            print("El numero {} no es un numero perfecto ".format(numero_int))
            print("")
    else:
        print("El numero debe ser mayor que cero ")
        print("")

    salir = input("Digite cualquier tecla para continuar o (S)alir ")


