# Ejercicio 1
palabra = input("Ingrese una palabra para repetirla: ")

for i in range(10):
    print(palabra)


# Ejercicio 2
edad = int(input("Ingrese su edad: "))

for i in range(edad):
    print(f"Viviste tu año {i +1}")


# Ejercicio 3
num = int(input("Ingrese un número positivo: "))
odd_list = []
if num < 0:
    input("Número ingresado inválido")
else:
    for i in range(1, num + 1, 2):
        odd_list.append(i)
    print(odd_list)


# Ejercicio 4
# Numero 4
number = int(input("Ingrese un numero entero positivo: "))
list = []
while number >= 0:
    list.append(number)
    number = number - 1
print(list)


# Ejercicio 5
to_invert = int(input("Ingrese la cantidad de dinero a invertir: "))
anual_int = int(input("Ingrese el interés anual: "))
total_years = int(input("Ingrese la cantidad de años: "))

years = 1
gains_t = 0

while years <= total_years:
    parcial_gains = 0
    gains_t = gains_t + (to_invert * (anual_int / 100))
    parcial_gains = parcial_gains + (to_invert * (anual_int / 100))
    to_invert += parcial_gains
    print(f"Las ganacias del año {years} son: ${gains_t}")
    print(f"Este año, en total tiene: ${to_invert}\n")
    years = years + 1


# Ejercicio 6
number = int(input("Ingrese un numero entero: "))
asterisk = ""
for i in range(number):
    asterisk += "*"
    print(asterisk)


# Ejercicio 7
number = int(input("Ingrese el numero de la tabla que quieres ver "))

for n in range (10):
    print( number,"x",n +1,"=",(number*(n+1)))


# Ejercicio 8
n = int(input('Ingresa un numero: '))
print()
string = ''
for i in range(n):
    if(i % 2 != 0):
        string = str(i) + ' ' + string
        print(string)


# Ejercicio 9
password = 'miContraseña'
pass_U = input('Ingresar contraseña:')
while pass_U != password:
    print('CONTRASEÑA INGRESADA INCORRECTA')
    pass_U = input('Ingresar contraseña nuevamente:')
print('CONTRASEÑA INGRESADA CORRECTA')


# Ejercicio 10
number = int(input('Ingresar un numero:'))
dividers = 0
for n in range(1, number+1):
    if number % n == 0:
        dividers += 1

if dividers == 2:
    print(f'{number} es un numero primo')
else:
    print(f'{number} no es un numero primo')


# Ejercicio 11
word = input('Ingresar una palabra:')
for l in reversed(word):
    print(l)


# Ejercicio 12
character = input('Ingresa un caracter: ')
phrase = input('Ingresa una frase: ')
charCount = 0
for i in phrase:
    if i == character:
        charCount += 1
print(charCount)


# Ejercicio 13
sent = input("Escribe lo que quieras: ")
array = []
cont = 0
while sent != "salir":
    array.append(sent)
    sent = input("Escribe lo que quieras: ")
    cont += 1
for i in range(cont):
    print(array[i])


# Ejercicio 14
a, b = int(input("Ingrese un numero: ")), int(input("Ingrese otro número : "))
even = []
odd = []
if a > b:
    ran = range(b, a+1)
else:
    ran = range(a, b+1)
for i in ran:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(f"Los números pares son: {even}. Los números impares son: {odd}")


# Ejercicio 15
n = int(input('Ingresa un numero mayor que cero para ver sus divisores: '))
for i in range(1, n+1):
    if n % i == 0:
        print(f'El numero {i} es divisor de {n}')

# Ejercicio 16
limit = int(input('Ingresa cuántos números vas a introducir: '))
empty_counter = 0
for i in range(limit):
    n = int(input(f'{i + 1}- Ingresa un número: '))
    if n < 0:
        empty_counter += 1
print(f'Ingresaste {empty_counter} números negativos')

# Ejercicio 17
empty_list = []
vocals = 'aeiou'
frase = input('Ingresa una frase: ')
for letra in frase:
    if letra in vocals and letra not in empty_list:
        empty_list.append(letra)
print(f'Las vocales usadas en la frase fueron: {empty_list}')

# Ejercicio 18. Fibonacci
fibonacci = [0, 1]
for i in range(2, 11):
    nuevo = fibonacci[i - 2] + fibonacci[i - 1]
    fibonacci.append(nuevo)
print(fibonacci)

# Ejercicio 19 (Alcancía)
objective = int(input('Ingresa la cantidad de dinero que deseas ahorrar: '))
receive = 0
while receive < objective:
    money = int(input('Dinero ingresado: '))
    if money > 0:
        receive += money
print(f'Felicitaciones, alcanzaste tu objetivo. Tu dinero ahorrado es de {receive}')

# Ejercicio 20. Sumatoria de Números
num = int(input("Ingresa un número: "))
sum = 0
while num != 0:
    sum += num
    num = int(input("Ingresa un número: "))
print(f'La sumatoria de todos los números distintos de cero ingresados es: {sum}')

# Ejercicio 21
print("Ingresa números enteros positivos. Para finalizar, ingresa 0.")
num = int(input("Número: "))
max_num = 0
while num > 0:
    if num > max_num:
        max_num = num
    num = int(input("Número: "))
print(f'El número más grande es: {max_num}')

# Ejercicio 22
num = int(input("Ingrese un número entero positivo: "))
even = 0
while num > 0:
    if num % 2 == 0:
        even += 1
    sum_of_digits = sum(int(digit) for digit in str(num))
    print(f"La suma de los dígitos es: {sum_of_digits}")
    num = int(input("Ingrese un número entero positivo: "))
print(f"En total ingresaste {even} números pares")

# Ejercicio 23
leave = 1
total_amount = 0
while leave != 0:
    price = int(input("Ingrese el monto del producto: "))
    total_amount += price
    if price == 0:
        leave = 0
print(f"El monto final de su compra es: {total_amount}")

# Ejercicio 24
leave = 1
total_amount = 0
while leave != 0:
    price = int(input("Ingrese el monto del producto: "))
    if price < 0:
        print("Monto inválido. \n Ingrese un nuevo monto")
    else:
        total_amount += price
        if price == 0:
            leave = 0
        if total_amount > 1000:
            total_amount -= total_amount * 0.1
print(f"El monto final de su compra es: {total_amount}")

# Ejercicio 25
number = int(input("Ingrese un número entero para conocer su factorial: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"El factorial de {number} es: {factorial}")
