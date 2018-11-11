'''
Escriba una función que permita determinar si un número se encuentra en un rango determinado
ej: is_in_range(num, min, max).
'''

print("========================================")
print("=    Ejercicio No. 2, Tarea No. 2      =")
print("=       Por: Guillermo Mora B.         =")
print("========================================")

print("")

#Funcion para solicitar los numeros al usuario
def solicitar_rango():
    num_str1 = input("Digite numero inferior del rango: ")
    num_str2 = input("Digite numero superior del rango: ")

    return(num_str1,num_str2)

#Funcion para convertir los string en integer
def convertir_numero(num1):
    num1 = int(num1)

    return(num1)

#Funcion para verificar si el numero esta en el rango
def verificar_numero(num1,num2,num3):
    if num1 >= num2 and num1 <= num3:
        si_esta = True
    else:
        si_esta = False

    return(si_esta)

#Funcion para verificar si el rango es correcto
def verificar_rango(num1,num2):
    correcto = False
    if num2 > num1:
        correcto = True

    return(correcto)


#Cuerpo del programa
salir = ""
while salir != "s" and salir != "S":

    #Solicitar numero al usuario
    numero_string1,numero_string2 = solicitar_rango()
    #Convertir string en int
    minimo = convertir_numero(numero_string1)
    maximo = convertir_numero(numero_string2)
    rango_ok = verificar_rango(minimo,maximo)

    if not rango_ok:
        print("El rango seleccinado es incorrecto")
    else:
        #Solicitar numero a verificar
        salir_2 = ""
        while salir_2 != "s" and salir_2 != "S":
            numero_string3 = input("Digite numero a verificar: ")
            numero = convertir_numero(numero_string3)
            existe = verificar_numero(numero,minimo,maximo)
            if existe:
                print("")
                print("El numero {} si se encuentra entre el numero {} y el numero {}".format(numero,minimo,maximo))
            else:
                print("El numero {} no se encuentra entre el numero {} y el numero {}".format(numero, minimo, maximo))

            print("")
            salir_2 = input("Digite cualquier tecla para verificar otro numero o (S)alir ")

    salir_2 = ""
    print("")
    salir = input("Digite cualquier tecla para definir un nuevo rango o (S)alir ")
    print("")

