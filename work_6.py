#Ejercicio 1
op = 1
list = []
while op != 0:
    op = int(input('Ingresa un numero para agregarlo a la lista, si quieres salir ingresa 0\n'))
    if op != 0:
        list.append(op)

print(list)

#EJERCICIO 2
op_delete = int(input('Ingresa un numero que quieras borrar de la lista, si el numero no esta en la lista, no podras borrarlo: '))

if op_delete in list:
    print('El numero si esta en la lista, procederemos a borrarlo')
    list.remove(op_delete)
else:
    print('El numero no esta en la lista')
print(list)

#EJERCICIO 3
suma = 0
for n in list:
    suma += n

print(f'la suma de los numeros de la lista es {suma}')

#EJERCICIO 4
new_num = input('Ingresa un numero, para crear una nueva lista de numeros que sean inferiores a ese numero:\n')

new_list = [n for n in list if n < int(new_num)]

print(new_list)

#EJERCICIO 5
element_count = {}
for num in list:
    if num in element_count:
        element_count[num] += 1
    else:
        element_count[num] = 1

tuple_list = [(element, count) for element, count in element_count.items()]


print(tuple_list)

#EJERCICIO 6

primary_school = []
high_school = []
names_primary=''
names_high=''
print('Ingresar los nombres de pila de los ALUMNOS DE PRIMARIA \n(Cuando no quiera ingresar mas nombres ingrese x):')
while names_primary!='X':
    names_primary=input()
    names_primary=names_primary.capitalize()
    if type(names_primary) is str and names_primary!='X':
        primary_school.append(names_primary)
    else:
        print("El valor ingresado no es una palabra")


print('Ingresar los nombres de pila de los ALUMNOS DE SECUNDARIA \n(Cuando no quiera ingresar mas nombres ingrese x):')


while names_high!='X':
    names_high=input()
    names_high=names_high.capitalize()
    if type(names_high) is str and names_high!='X':
        high_school.append(names_high)
    else:
        print("El valor ingresado no es una palabra")


#OBTENER NOMBRES DE NIVEL PRIMARIO SIN REPETICION
repeated_primary=[]
without_repeating_primary=[]


for a in primary_school:
    counter=primary_school.count(a)
    if counter>1 and a not in repeated_primary:
        repeated_primary.append(a)
    elif counter==1 and a not in without_repeating_primary:
        without_repeating_primary.append(a)


for name in repeated_primary:
    without_repeating_primary.append(name)
print("NIVEL PRIMARIO")
for a in without_repeating_primary:
    print(f"-{a}" )




#OBTENER NOMBRES DE NIVEL SECUNDARIO SIN REPETICION
repeated_high=[]
without_repeating_high=[]


for a in high_school:
    counter=high_school.count(a)
    if counter>1 and a not in repeated_high:
        repeated_high.append(a)
    elif counter==1 and a not in without_repeating_high:
        without_repeating_high.append(a)


for name in repeated_high:
    without_repeating_high.append(name)
print("NIVEL SECUNDARIO")
for a in without_repeating_high:
    print(f"-{a}" )


#NOMBRES REPETIDOS
print("Nombres repetidos nivel PRIMARIO")
for a in repeated_primary:
        print(f"-{a}")


print("Nombres repetidos nivel SECUNDARIO")
for a in repeated_high:
        print(f"-{a}")


#NOMBRES DEL NIVEL PRIMARIO QUE NO SE REPITEN EN EL SECUNDARIO
not_in_high_school = []


for name in without_repeating_primary:
    repeat = False
    for a in without_repeating_high:
        if name == a:
            repeat = True
            break
    if not repeat:
        not_in_high_school.append(name)


print("Estudiantes del primario que no se repiten en el secundario")
for student in not_in_high_school:
    print(student)

#EJERCICIO 7

phrase_list = []



def count_characters(phrase_list):
    dic_letters = {}
    for sentence1 in phrase_list:
        for letter1 in sentence1:
            dic_letters[letter1] = 0


    for sentence2 in phrase_list:
        for letter2 in sentence2:
            if letter2 in dic_letters:
                dic_letters[letter2] += 1
    for clave, value in dic_letters.items():
        print(f"El carácter {clave} aparece: {value} veces.")
phrase_list = []
for i in range(3, 0, -1):
    phrase = input(f"Ingrese {i} oraciones: ")
    phrase_list.append(phrase)
    count_characters(phrase_list)
#EJERCICIO 8
#lista de listas de goles de cada equipo:
goal_list=[(0,4,2,1,2,3,1,2,3,0),(5,0,3,2,2,0,0,3,1,2),(0,2,0,1,3,0,1,2,4,2),(1,0,2,0,1,2,3,1,1,0),(1,1,2,1,0,2,1,3,0,3),(1,2,3,1,0,0,2,4,3,1),(4,5,0,0,2,4,0,1,2,1),(2,2,1,0,3,1,3,0,1,1),(0,2,1,0,3,4,5,1,0,2),(0,2,3,3,1,0,0,3,1,0)]


#"Goles de cada equipo:"
print("Goles de cada equipo:")
i=1
for team in goal_list:
    print(f"Equipo {i}: {team}")
    i+=1


# Cantidad de triunfos por equipo
# Total de goles realizados y recividos por equipos
print("-----------------------------")
for i in range(10):
    victory=0
    defeat=0
    tie=0
    goals_scored=0
    goals_against=0
    print(f"partidos del equipo: {i+1}")
    for j in range(10):
        #Total de goles realizados y recividos por equipos
        goals_scored+=goal_list[i][j]
        goals_against+=goal_list[j][i]
        # Cantidad de triunfos por equipo
        if(i!=j):
            if(goal_list[i][j]>goal_list[j][i]):
                victory+=1
            elif(goal_list[i][j]<goal_list[j][i]):
                defeat+=1
            else:
                tie+=1
    print(f"Victorias: {victory}\nDerrotas:{defeat}\nEmpates: {tie}")
    print(f"Total de goles marcados: {goals_scored}\nTotal de goles recibidos: {goals_against}\nPuntos: {victory*3 + tie}\n-----------------------------")

#EJERCICIO 9

#Imprime las filas y columnas de una forma mas bonita visualmente
def prin_cards(cards):
    for i in range(len(cards)):
        print(f"{cards[i][0]} {cards[i][1]} {cards[i][2]} {cards[i][3]} {cards[i][4]} {cards[i][5]}   ")


#Coloca los símbolos en posiciones aleatoreas cada vezz que se inicia el juego
import random as ran
def posicionate_characters():
    #lista de símbolos
    char = ["♥", "♠", "♣", "♦", "♫", "۞", "§", "Ŧ", "Ʃ", "♥", "♠", "♣", "♦", "♫", "۞", "§", "Ŧ", "Ʃ"]
    #Mezcla los elementos de la lista de forma aleatoria
    ran.shuffle(char)
    cards = [[],
        [],
        []
        ]
    #Distribuye los elementos de carácteres en una matriz de 3x3
    for i, select_char in enumerate(char):
        cards[i % 3].append(select_char)
    #Devuelve la matriz 3x3 con los elementos en ella
    return cards


#comprueba que el número ingresado no esté adivinado
def comprb_valid_num(msg, numeros_correctos):
    while True:
        numero = int(input(msg))
        if numero in numeros_correctos:
            print("Ya se adivinó ese número")
        else:
            return numero


#encuentra el símbolo en la posicion pasada por el usuarioy devuelve la lista de "?" con el símbolo en su respectiva posicion
def find_card1(position, enigm, card):
    row = (position -1) // 6
    column = (position - 1) % 6
    enigm[row][column] = card[row][column]
    return enigm


#compara las posiciones ingresadas por el usuario y si son iguales muestra un mensaje y las parejas de cartas adivinadas se mostrarán el resto del juego.
def compare_cards(u_try, u_compare, enimg, card, to_convert, correct):
    row1 = (u_try -1) // 6
    column1 = (u_try - 1) % 6
    row2 = (u_compare -1) // 6
    column2 = (u_compare - 1) % 6
    if card[row1][column1] == card[row2][column2] and u_try != u_compare:
        print("\nCoincidencia!\n")
        enimg[row1][column1] = card[row1][column1]
        enimg[row2][column2] = card[row2][column2]
        to_convert[row2][column2] = "√"
        to_convert[row1][column1] = "√"
        correct = True
    else:
        print("\nNo hay coincidencia :(\n")
        enimg[row1][column1] = "?"
        enimg[row2][column2] = "?"
        correct = False
    return (enimg, to_convert, correct)

#lista de los números ya adivinados correctamente
list_of_correct_nums = []

#mientras todavia no haya adivinado todos los elementos el código se ejecutará
while "?" in [item for row in enigm_cards for item in row]:
    print()
    prin_cards(to_adivinate)
    while True:
        try:
            coincidence = False

            #el usuario ingresa una posicion a adivinar
            user_try = comprb_valid_num("Ingrese un número para ver la figura: ", list_of_correct_nums)

            prin_cards(find_card1(user_try, enigm_cards, cards))

            print()

            user_compare =comprb_valid_num("Ingrese un número para comparar la figura: ", list_of_correct_nums)

            prin_cards(find_card1(user_compare, enigm_cards, cards))

            print()

            #compara los simbolos de las posiciones, si son iguales se guardan
            enigm_cards, to_adivinate, coincidence = compare_cards(user_try, user_compare, enigm_cards, cards, to_adivinate, coincidence)
            if coincidence == True:
                list_of_correct_nums.append(user_try)
                list_of_correct_nums.append(user_compare)
            break
        except ValueError:
            print("Ingrese un número del 1 al 18")
print("Felicidades has adivinado todos los símbolos!")

#EJERCICIO 10
def calc_diagonal(matriz):
    matriz_rows = len(matriz)
    diag = []
    i = 0
    while i < matriz_rows:
        diag.append(matriz[i][i])
        i += 1
    return diag


#Pone en una lista la diagonal inversa de una matriz
def calc_inv_diagonal(matriz):
    inv_position = len(matriz) - 1
    i = 0
    inv_diag = []
    while inv_position > i-1:
        inv_diag.append(matriz[inv_position][inv_position])
        inv_position -= 1
    return inv_diag

first_matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
diagonal =calc_diagonal(first_matrix)
print(diagonal)


inv_diagonal =calc_inv_diagonal(first_matrix)
print(inv_diagonal)

#EJERCICIO 11
coin_dictionary = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
currency = input("Ingrese el nombre de una divisa: ").title()
if currency in coin_dictionary:
    print(coin_dictionary[currency])
else:
    print("La divisa no está registrada")

#EJERCICIO 12
# Crear un diccionario vacío para almacenar la información del usuario
user = {}


# Pedir al usuario que ingrese su nombre, edad, dirección y teléfono
user['nombre'] = input('Ingrese su nombre: ')
user['edad'] = input('Ingrese su edad: ')
user['dirección'] = input('Ingrese su dirección: ')
user['telefono'] = input('Ingrese su número de teléfono: ')


# Mostrar la información del usuario por pantalla
mensaje = '{} tiene {} años, vive en {} y su número de teléfono es {}.'
print(mensaje.format(user['nombre'], user['edad'], user['dirección'], user['telefono']))

#EJERCICIO 13
precios_frutas = {
    'manzana': 1.5,  # Precio por kilo de manzana
    'banana': 2.0,   # Precio por kilo de banana
    'pera': 1.8,     # Precio por kilo de pera
    # Agrega más frutas y sus precios aquí
}




# Pedir al usuario que ingrese la fruta y la cantidad de kilos
fruta = input('Ingrese el nombre de la fruta: ')
kilos = float(input('Ingrese la cantidad de kilos: '))


# Verificar si la fruta está en el diccionario
if fruta in precios_frutas:
    # Calcular el precio total
    precio_total = precios_frutas[fruta] * kilos
    #resultado
    mensaje = 'El precio de {} kilos de {} es: ${:.2f}'
    print(mensaje.format(kilos, fruta, precio_total))
else:
    # Mostrar un mensaje si la fruta no está en el diccionario
    print('Lo siento, no tenemos el precio para la fruta ingresada.')