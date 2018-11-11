'''
Cree una función en Python que reciba tres números y retorne el mayor de los tres.
'''

print("========================================")
print("=    Ejercicio No. 1, Tarea No. 2      =")
print("=       Por: Guillermo Mora B.         =")
print("========================================")

print("")
#Funcion para solicitar los numeros al usuario
def solicitar_numeros():
    num_str1 = input("Digite un numero: ")
    num_str2 = input("Digite otro numero: ")
    num_str3 = input("Digite un ultimo numero: ")

    return(num_str1,num_str2,num_str3)

#Funcion para convertir los string en integer
def convertir_numero(num1,num2,num3):
    num1 = int(num1)
    num2 = int(num2)
    num3 = int(num3)

    return(num1,num2,num3)

#Funcion para determinar el numero mayor
def numero_mayor_f(num1,num2,num3):
    if num1 > num2:
        if num1 > num3:
            mayor = num1
    elif num2 > num3:
        mayor = num2
    else:
        mayor = num3

    return(mayor)


#Cuerpo del programa
salir = ""
while salir != "s" and salir != "S":

    #Solicitar numero al usuario
    numero_string1,numero_string2,numero_string3 = solicitar_numeros()
    #Convertir string en int
    numero_int1,numero_int2,numero_int3 = convertir_numero(numero_string1,numero_string2,numero_string3)
    #Determinar numero mayor
    numero_mayor = numero_mayor_f(numero_int1,numero_int2,numero_int3)
    print("")
    print("El mayor numero entre {}, {}, {} es el numero {}".format(numero_int1,numero_int2,numero_int3,numero_mayor))
    print("")
    salir = input("Digite cualquier tecla para continuar o (S)alir ")
    print("")

