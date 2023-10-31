#Ejercicio--1---------------------------------------------------------------------------

#Funciones
def count_digits(n, digits):
    s = str(n)
    if len(s) <= 1:
        return digits
    else:
        digits += 1
        return count_digits(s[:-1], digits)


#Código principal
import aFunciones as funcion
digit = 1
num = int(input("Ingrese un número: "))
print(funcion.count_digits(num, digit))

#ejercicio---2-------------------------------------------------------------------------

def potencia1(n,b):
    if(n>b):
        return potencia(n/b,b)
    elif(n==b):
        return True
    else:
        return False




print("Bienvenido: ")
print("Para saber si un número entero [n] es potencia de otro número entero [b]")
n = int(input("Por favor ingrese un número entero para [n]: "))
b = int(input("Por favor ingrese otro número entero para [b]: "))
potency = potencia1(n,b)
if potency == True:
    print(f"El número {n} es potencia de {b}")
else:
        print(f"El número {n} no es potencia de {b}")

#Ejercicio--3-----------------------------------------------------------------------------
#función
def string_position(a, b, start = 0):
    count = []
    index = a.find(b, start)
    if index != -1:
        count.append(index)
        count += string_position(a, b, index + 1)
    return count

#Código principal
import aFunciones as funcion
print(funcion.string_position("pablito clavó un clavito, cuantos clavitos clavó pablito", "ito"))

#ejercicio--4-------------------------------------------------------------------------------
#Funciones
def par(n):
    if n == 1:
        return False
    else:
        return impar(n-1)
    


def impar(n):
    if n == 1:
        return True
    else:
        return par(n-1)

#codigo principal

print("Bienvenido: por favor ingrese una opición: ")
while True:
    option = input("Ingrese [1] para saber de forma recursiva  si un número es par o ingrese [2] para saber si un número es impar: ")
    try:
        if (option.isdigit()) and (option == "1" or option == "2"): 
            option =  int(option)
            
            if option == 1:
                print("Usted seleccionó par. ")
            else:
                print("Usted seleccionó impar. ")
            n = int(input("Ingrese un número natural: "))
            if n > 0:
                break
            else:
                print("Datos ingresados incorrectos. Reintente. ")
    except:
        print("Debe ingresados incorrectos. Reintente.  ")


if option == 1:
    print(f"¿El número {n} es par? {par(n)}")
elif option == 2:
    print(f"¿El número {n} es impar? {impar(n)}")


#Ejercicio--5------------------------------------------------------------------------
def found_bigest(nums, mayor = None, i = 0):
    if i == len(nums):
        return mayor
    else:
        if mayor is None or nums[i] > mayor:
            mayor = nums[i]
    return found_bigest(nums, mayor, i+1 )

#Ejercicio--6----------------------------------------------------------------------------------
#Funciones
def repli(nums, n, index = 0):
    if index == (len(nums)):
        return []


    num_list = []
    for i in range(n):
        num_list.append(nums[index])

    return num_list + repli(nums, n, index + 1 )

#Código principal
import aFunciones as funcion
replic_list = funcion.repli([1,3,3,7], 4)
print(replic_list)
#Ejercicio--7----------------------------------------------------------------------------------------------------
#Funciones
def calcular_K(n, p):
    if n == 1:
        return p
    else:
        return n * p + calcular_K(n-1, p)

#codigo principal

n = int(input("Ingrese el valor de n: "))
p = int(input("Ingrese el valor de p: "))

resultado = calcular_K(n, p)
print(f"El resultado de K({n}, {p}) es: {resultado}")

#Ejercicio--8-------------------------------------------------------------------------------------------
def pascal(n, k):
    if k == 0 or k == n:
        return 1
    else:
        return pascal(n-1, k-1) + pascal(n-1, k)

# Ejemplo de uso
n = int(input("Ingrese el valor de n: "))
k = int(input("Ingrese el valor de k: "))

resultado = pascal(n, k)
print(f"El valor en la fila {n} y columna {k} del Triángulo de Pascal es: {resultado}")

#Ejercicio--9---------------------------------------------------------------------------------------

def combinations_helper(characters, k, current_combination, result):
    if len(current_combination) == k:
        result.append(current_combination)
        return

    if len(current_combination) > k:
        return  # Salir si la combinación actual supera la longitud máxima

    for char in characters:
        # Evita caracteres repetidos en la combinación
        if char not in current_combination:
            new_combination = current_combination + char
            combinations_helper(characters, k, new_combination, result)


def combinations(characters, k):
    if len(set(characters)) < len(characters):
        return 'La lista no puede contener caracteres repetidos'

    result = []
    combinations_helper(characters, k, "", result)
    for combination in result:
        print(combination)

combinations(['a', 'b', 'c','d'], 1)



#Ejercicio 10-------------------------------------------------------------------------------------
def medidas_hoja_A(n, count = 0):
    
    if n == 0:
        if count == 10:
            return (26,37)
        elif count == 9:
            return (37,52)
        elif count == 8:
            return (52,74)
        elif (count == 7):
            return (74,105)
        elif (count == 6):
            return (105,148)
        elif (count == 5):
            return (148,210)
        elif (count == 4):
            return (210,297)
        elif (count == 3):
            return (297,420)
        elif (count == 2):
            return (420,594)
        elif (count == 1):
            return (594,841)
        elif (count == 0):
            return (841,1189)
    else:
        return medidas_hoja_A(n-1, count + 1)

print("Bienvenido: ")
while True:
    try:
        n = int(input("Para conocer el ancho y el largo de la hoja que tiene Serie A, ingrese su número: "))
        if (n > -1) & (n < 11):
            break
        else:
            
            print("Debe ingresar valores entre cero [0] y diez [10]")
    except:
        print("Valores ingresados incorrectos. ")


print(f"La hoja A{n} de la Serie A tiene el suguiente ancho y largo: {medidas_hoja_A(n)}")

