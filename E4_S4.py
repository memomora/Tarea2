'''
Cree una función que se llame round_sum(num_a, num_b, num_c). La función round_sum
recibe 3 números enteros. Para cada uno de estos números enteros, la función debe redondearlos
a la decena más cercana (ejemplo: si un número es 15, entonces se redondea a 20, pero si es 14, se
redondea a 10) y luego debe sumar los números redondeados y devolver el resultado. El
programa debe utilizar funciones de responsabilidad única por lo que debe modularizar su
solución.
'''

print("==============================================")
print("=          Ejercicio No. 4, Semana 4         =")
print("=                    Por:                    =")
print("=              Guillermo Mora B.             =")
print("==============================================")
print("")

#Funcion para determinar si se digito un numero
def verifica_si_es_numero(num_str):
    esta_bien = True
    for indice in (num_str):
        numero_cadena = indice

        if (numero_cadena != "0" and numero_cadena != "1" and numero_cadena != "2" and numero_cadena != "3" and numero_cadena != "4" and
            numero_cadena != "5" and numero_cadena != "6" and numero_cadena != "7" and numero_cadena != "8" and numero_cadena != "9"):
            if esta_bien == True:
                esta_bien = False

    return(esta_bien)


#Funcion para solicitar los datos al usuario
def solicita_datos():
    print("==============================================")
    print("=             Solicitud de datos             =")
    print("==============================================")
    print("")

    numero_cadena = ""
    cantidad_veces = 3

    #Este ciclo solicita los datos al usuario hasta que este digite "s" o "S"
    while cantidad_veces > 0 :
        dato = input("Digite un numero: ")
        verifica_numero = verifica_si_es_numero(dato)

        if verifica_numero:
            numero_cadena = numero_cadena + dato +"," #En esta variable se va formando la cadena de numeros
            cantidad_veces -= 1
        else:
            print("Se deben digitar numeros")
            print("")

    return numero_cadena

def convertir_numero(numero_str):
    numero_str = int(numero_str)
    return numero_str

def determina_redondeo(numero_str):
    redondeo_superior = False

    unidades_del_numero = numero_str[len(numero_str)-1]
    unidades_del_numero = convertir_numero(unidades_del_numero)
    if unidades_del_numero >= 5:
        redondeo_superior = True

    return redondeo_superior

#Funcion para procesar la cadena de numeros y obtener la suma de los redondeos
def procesar_cadena(cadena):
    numero_cadena = ""
    sumar_redondeo = 0
    for indice in range (len(cadena)):
        if cadena[indice] != ",": #cada numero esta separado por comas
            numero_cadena = numero_cadena + cadena[indice] #en esta variable se van formando los numeros a partir de la cadena
        else:
            numero_int = convertir_numero(numero_cadena)
            numero_sumar_restar = numero_cadena[len(numero_cadena) - 1]
            numero_sumar_restar = convertir_numero(numero_sumar_restar)
            redondeo_suerior = determina_redondeo(numero_cadena)
            if redondeo_suerior:
                numero_int = (numero_int - numero_sumar_restar) + 10
                sumar_redondeo = sumar_redondeo + numero_int
                numero_cadena = ""
            else:
                numero_int = numero_int - numero_sumar_restar
                sumar_redondeo = sumar_redondeo + numero_int
                numero_cadena = ""

    return sumar_redondeo


#Cuerpo del programa
salir = "" #Variable para controlar el ciclo de reproduccion del programa
while salir != "s" and salir != "S":
    cadena_numeros = solicita_datos() #se forma la cadena de numeros
    resultado_suma = procesar_cadena(cadena_numeros)

    print("La suma de los redondeos de los numeros es {}.".format(resultado_suma))
    print("")
    salir = input("Digite <ENTER> para continuar o (S)alir) ")
