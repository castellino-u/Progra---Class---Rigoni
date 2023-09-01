#Elementos iteradores: string, lista, tupla, dict

#Ejercicio 1: 
abecedario = "abcdefghijklmnñopqrstuvwxyz"
corrimiento = int(input("Ingrese la cantidad de lugares que se correran las letras: "))
for i in range(5) :
    msj_a_encriptar = input("Ingrese el mensaje a encriptar: ")
    palabra_encrip= ""
    for letra in msj_a_encriptar:
        if letra in abecedario:
            indice = abecedario.find(letra)
            indice_encrip = (indice + corrimiento) % 27
            palabra_encrip += abecedario[indice_encrip]
        else:
            palabra_encrip += letra
    print(palabra_encrip)

#Ejercicio 2
import math   #este math solo es necesario si vamos a usar la formula con math.floor comentada abajo

#Aca iniciamos las variables y pedimos una entrada de datos
contador_pares_totales = 0
contador_impares_totales = 0
numeros_positivos = 1
numeros_positivos = int(input("Ingrese un numero entero positivo para conocer sus digitos pares e impares:  "))
 
#iniciamos los ciclos while
while numeros_positivos != 0:
    #contadores parciales que se van a reiniciar en cada vuelta del while principal
    contador_pares = 0
    contador_impares = 0

    
    while numeros_positivos > 0:
        proceso = numeros_positivos % 10   #procedimiento para obtener el ultimo digito de cada numero 
        
        if (proceso % 2) == 0:             #if para obtener los pares e impares
            contador_pares+= 1
            contador_pares_totales += 1
        else:
            contador_impares += 1
            contador_impares_totales += 1
        numeros_positivos= int(numeros_positivos / 10)   #procedimiento para ir cortando el ultimo digito del numero hasta llegar a cero 
        #se puede hacer con la formula de arriba o con la formula de abajo, ambas funcionan
        #numeros_positivos= math.floor(numeros_positivos / 10)
    print(contador_pares, " numeros pares y ", contador_impares, " numeros impares")    

    numeros_positivos = int(input("Ingrese otro numero entero positivo para continuar o 0(cero) para terminar: ")) #reentrada de datos para continuar o cortar el ciclo
print("Total de pares: ", contador_pares_totales, " y Total de impares: ", contador_impares_totales) #muestra los digitos pares e impares totales
        