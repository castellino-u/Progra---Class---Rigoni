#EJERCICIO 1
def validDni(num):
    if len(str(num)) == 7 or len(str(num)) == 8:
        return True
    else:  
        return False

#EJERCICIO 2
def longitud_ultima_palabra(cadena):
    cadena = cadena.strip()
    palabras = cadena.split()
    if palabras:
        ultima_palabra = palabras[-1]
        return len(ultima_palabra)
    else:
        return 0

#EJERCICIO 3    
def validDni(num):
    if len(str(num)) == 7 or len(str(num)) == 8:
        return True
    else:  
        return False

def searchLastName(entryName):
    if len(entryName) >= 3:
        return  entryName[2]
    elif len(entryName) == 2:
        return entryName[1]

def getDniId(dni):
    if len(str(dni)) == 8:
        return dni // 100000
    else:
        return dni // 10000

def createId(name, lastName, numId):
    prevId = ""
    prevId += name[0] + str(len(lastName)) + str(numId)

#EJERCICIO 4
def Multiples(a,b):
    if a % b == 0:
        return True
    else:
        return False

#EJERCICIO 5
def calc_median(max, min):
    median = (max + min) / 2
    return median

#EJERCICIO 6
def space_between_letters(word):
    spaced_word = ''.join([c + ' ' for c in word if c != ' '])
    return spaced_word

#EJERCICIO 7
def calc_min_and_max(num_list):
    n_min = 100000000000000000
    n_max = 0
    for i in range(len(num_list)):
        if num_list[i] < n_min:
            n_min = num_list[i]
        elif num_list[i] > n_max:
            n_max = num_list[i]
    return n_min, n_max

#EJERCICIO 8
import math
def calc_circumference(circumference):
    circumference = float(circumference)
    radius =  circumference / (2 * math.pi)
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return radius, area, perimeter

#EJERCICIO 9
def login(user, password):
    login_ok = 0
    if user == "usuario1" and password == "asdasd":
        login_ok = 1
    return login_ok

#EJERCICIO 10
def purchase_total(prices_percentages):
    prices=list(prices_percentages.keys())
    percentages=list(prices_percentages.values())
    total=0
    for n in range(len(prices)):
        calculation=prices[n]*(1-percentages[n])
        total+=calculation
    return total

#EJERCICIO 11
def swap(names):
    apply_change = ""
    apply_change = names.swapcase()
    return apply_change

def call_other_f(names):
    change_name = ""
    change_name = swap(names)
    return change_name

#EJERCICIO 12
def phrase_to_dict(phrase):
    new_dict = {}
    temporal_array = phrase.split(" ")
    for word in temporal_array:
        new_dict[word] = len(word)
    return new_dict

#EJERCICIO 13
import math
def calc_modulo_vector(array):
    aux_sum = 0
    for i in array:
        aux_sum += i**2
    modul = math.sqrt(aux_sum)
    return modul

#EJERCICIO 14
def verify_prime_number(num):
    divisors = 0
    for i in range(num, 0, -1):
        if num % i == 0:
            divisors += 1
    if divisors <= 2:
        return True
    else:
        return False

#EJERCICIO 15
def calc_factorial(num):
    fact = 1
    if num == 0:
        fact = 1
    else:
        for i in range(1, num + 1):
            fact *= i
    return fact

def calc_entries(aux_num):
    if aux_num >= 0:
        return 1

#EJERCICIO 16
def separate_num(num):
    aux = list(str(num))
    return aux

def determ_frec(dig, frec, separate_num):
    for i in separate_num:
        if dig == i:
            frec +=1
    return frec

#EJERCICIO 17
def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def entering_prime_numbers():
    most_number = 0
    while True:
        num = int(input('Ingresa un numero primo, la lectura finalizara cuando ingreses un numero no primo:\n'))
        if is_prime(num):
                prime_sum = 0
                digit_frecuence = 0
                for digit in str(num):
                    prime_sum += int(digit)
                print(f'La suma de los digitos del numero primo ingresado es: {prime_sum}')
                opt_frecuence = input('Ingresa un digito del cual quieres saber la frecuencia en el numero ingresado:\n')
                for digit in str(num):
                    if digit == opt_frecuence:
                        digit_frecuence += 1
                if num > most_number:
                    most_number = num
                print(f'La frecuencia del digito "{opt_frecuence}" en "{num}" es: {digit_frecuence}')
        else:
            print(f'El numero ingresado no es primo, el mayor numero que ingresaste en esta sesion fue "{most_number}"  y su factorial es: {math.factorial(most_number)}\n Saliendo...')
            break

