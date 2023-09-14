#Ejercicio 1
    #Create a while loop with the following characteristics: 

        #• The initial value of the variable x will be 0.
        #• The increment value will be 1.
        #• The exit condition of the loop will be greater than or equal to 30.
        #• The execution must be broken when x is equal to 15.
        #• You must print the following sentence each time the loop executes: 'The value of the loop is: ' + x.
        #• You must skip the executions with the value of x in 4, 6 and 10.
        #• At each execution jump, you must display the jumped values with this message: 'The value ' + x ' of x was skipped'.
        #• When the execution of the loop is broken, you must show a message indicating it: 'The execution of the loop was broken when x was ' + x.

x = 0
while x <= 30:
    x += 1
    if x == 4 or x == 6 or x == 10:
        print('The value ' + str(x) + ' of x was skipped')
        pass
    else:
        print('The value of the loop is: '+ str(x))
    if x == 15:
        print('The execution of the loop was broken when x was ' + str(x))
        break

#Ejercicio 1 en español
    #Escriba un programa que acepte una secuencia de líneas e imprima todas las líneas convertidas en mayúsculas. 
    # Deje una línea en blanco para indicar que ha finalizado la entrada de líneas.

sentence= input("Escribe una oración: ").upper()
while sentence:
  if sentence[-1]==" ":
    break
  sentence+=". "+ input("Escribe una oración: ").upper()
print(sentence)

#Ejercicio 2: 
    #Escriba un programa que administre una cuenta bancaria, usando una bitácora de operaciones.
    #La bitácora de operaciones tiene la siguiente forma: (Thomy)
    #D 100
    #R 50

    #D 100 significa que depositó 100 pesos
    #R 50 significa que retiró 50 pesos

    #Ejemplo de una entrada:
    #D 200
    #D 200
    #R 100
    #D 50
    #Introducir una línea vacía indica que ha finalizado la bitácora.
    #La salida de éste programa sería:
    #350

balance = 0
logbook = "\n"
entry = "."
while entry != "":
    print("\n")
    entry = input("¿Qué operación desea realizar? \n Deposito(D) --- Retiro(R), e ingrese el monto.\n Para finalizar presione enter: ")
    
    if entry != "":
        operation = entry[0]
        entry = entry.split()
        del entry[0]
        sum = int(entry[0])
        operation = operation.upper()
    if operation == "D":
        deposit = sum
        logbook = logbook + f"D {deposit} \n"
        balance = balance + deposit
    elif operation == "R":
        whitdrew = sum
        if balance - whitdrew < 0:
            print("Saldo insuficiente \n")
        else:
            logbook = logbook + f"R {whitdrew} \n"
            balance = balance - whitdrew
    else:
        print("Operación ingresada inválida \n")


print(f"Bitácora: \n {logbook}")


print(f"Saldo final: {balance}")

#Ejercicio 3
    #Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, finalizando cuando se reciba un cero.
    #Imprimir la cantidad total de números primos ingresados.
    #Nota: Un número primo es un número natural mayor que 1 que tiene únicamente dos divisores distintos: él mismo y el 1.
numbers=[]
escape=1
number_prime=0
while escape==1:
    num=int(input('Ingresar numero:'))
    if num>=1:
        numbers.append(num)
        divisor=0
        for n in range(1,num+1):
            if num%n==0:
                divisor+=1
        if divisor==2:
            number_prime+=1
    elif num==0:
        break
    else:
        print('Ingresar numeros positivos')
   
print(f'Numero ingresados:{numbers}')
print(f'Numeros primos:{number_prime}')

#Ejercicio 4 
    #Escribir un programa que permita al usuario ingresar dos años y luego imprima todos los años en ese rango, que sean bisiestos y múltiplos de 10.
    #Nota: Para que un año sea bisiesto debe ser divisible por 4 y no debe ser divisible por 100, excepto que también sea divisible por 400.

year1 = int(input("Ingrese el primer año: "))
year2 = int(input("Ingrese el segundo año: "))
year_list = []
year_mult = []

for i in range(year1, year2 + 1):
    if (i % 4 == 0) and i % 100 != 0 or i % 400 == 0:
        year_list.append(i)
    elif i % 10 == 0:
        year_mult.append(i)


print(f"Los años bisiestos entre los ingresados son: {year_list} ")
if len(year_mult) != 0:
    print("Los años multiplos de 10 son: ", year_mult)

#Ejercicio 5 
    #Escribe un programa que imprima todos los números pares del 1 al 20 usando un bucle for.
    #Utiliza la declaración continue para omitir los números impares.
for i in range(1,21):
    if i % 2 != 0:
        continue
    else:
        print(i)

#Ejercicio 6
    #Crea una lista de números y utiliza un bucle for para encontrar un número específico.
    #Cuando encuentres el número, usa break para salir del bucle.
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
search= int(input("Ingrese el numero que desea buscar:"))
for i in list:
   
    if search in list:
        print("Lo encontre!")
        break
    else:
        print("El numero no esta en la lista ")

#Ejercicio 7:
    #Crea un programa que muestre un menú de opciones (por ejemplo, opciones 1, 2, 3).
    #Utiliza un bucle while para permitir al usuario seleccionar una opción. 
    #Si el usuario ingresa "0", utiliza break para salir del bucle (Mostrar un mensaje por cada opción elegida)

print("Bienvenido al sistemas de menú interactivo")
option = 5
print("menú 1: Atencion ")
print("menú 2: Trámites ")
print("menú 3: Consultas ")
while option != 0:
    option_1 =int(input("Por favor ingrese 1(uno), para el menú 1. Ingrese 2(dos), para el menú 2. Ingrese 3(tres) para el menú 3 o ingrese 0(cero) para salir: "))
    if option_1 == 0:
        print("Usted ha ingresado 0 para salir del programa. Hasta pronto. ")
        break
    elif option_1 == 1:
        print("Usted ha ingresado 1.  Atención: ...")
    elif option_1 == 2:
        print("Usted ha ingresado 2. Trámites: ... ")
    elif option_1 == 3:
        print("Usted ha ingresado 3. Consultas: ...")
    else:
        print("La opción ingresada no corresponde, inténtelo nuevamente. ")
