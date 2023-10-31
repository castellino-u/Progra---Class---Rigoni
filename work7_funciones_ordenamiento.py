#Ejercicio 1
def bubble_sort(numList: list) -> list:
    init = 0
    next = 1
    for i in range(len(numList)):
        for j in range(i + 1, len(numList)):
            if numList[i] > numList[j]:
                numList[i], numList[j] = numList[j], numList[i]
    return numList

print(bubble_sort([1,100,2]))

#Ejercicio 2
word_list = ['Pepito', 'Rodrigo', 'Anana', 'Queso']


def selection_sort_word_list(arr: list) -> list:
    n = len(arr)

    # Iterar a través de todos los elementos de la lista.
    for i in range(n):
        # Suponemos que el primer elemento no ordenado es el mínimo.
        min_idx = i

        # Comparamos el elemento actual con el mínimo encontrado hasta ahora.
        for j in range(i + 1, n):
            if arr[j].lower() < arr[min_idx].lower():
                min_idx = j

        # Intercambiamos el elemento mínimo con el elemento en la posición i.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print(selection_sort_word_list(word_list))
#Ejercicio 3
def order_books(to_order, book):
    large = len(to_order)
    for i in range(0,large):
        for j in range(0,large):
            if to_order[j] > to_order[i]:
                book[i], book[j] = book[j] , book[i]
    return book

books = [{
    "titulo":"libro 1",
    "fecha":1998,
    "autor": "Pepe"
},
{
    "titulo":"Mordida",
    "fecha":1987,
    "autor": "Scot"
},
{
    "titulo":"JoJo SBR",
    "fecha":2004,
    "autor": "Araki"
}]
print("Ordenados por autor")
authors = []
for i in range(0, len(books)):
    for keys in books[i]:
        if keys == "autor":
            authors.append(books[i][keys])
print(authors)
print(order_books(authors, books))

#Ejercicio 4
def insertion_sort_large(to_order):
    for i in range(1, len(to_order)):
        key = to_order[i]  
        j = i - 1  


        while j >= 0 and len(key) < len(to_order[j]):
            to_order[j + 1] = to_order[j]
            j -= 1


        to_order[j + 1] = key
    return to_order

sentences_list = ["Manzana", "manzana","Vaca muerta", "palanca", "Pablo falleció", "Uva", "America no existe", "Spiderman", "España", "Se ha quemado mi casa", "Baul"]


print(insertion_sort_large(sentences_list))

#Ejercicio 5
def bubble_sort_desc(numList: list) -> list:
    init = 0
    next = 1
    for i in range(len(numList)):
        for j in range(i + 1, len(numList)):
            if numList[i] < numList[j]:
                numList[i], numList[j] = numList[j], numList[i]
    return numList


print(bubble_sort_desc([1,100,2,7]))
#Ejercicio 6
def counting_sort(arr):
    # Encontrar el valor máximo en la lista para determinar el rango.
    max_value = max(arr)

    # Crear una lista de conteo para contar la frecuencia de cada elemento.
    count = [0] * (max_value + 1)

    # Contar la frecuencia de cada elemento en la lista de entrada.
    for num in arr:
        count[num] += 1

    # Construir la lista ordenada a partir del conteo.
    sorted_arr = []
    for i in range(max_value + 1):
        while count[i] > 0:
            sorted_arr.append(i)
            count[i] -= 1

    return sorted_arr


print(counting_sort([4, 2, 2, 8, 3, 3, 1]))
#Ejercicio 7
def num_and_string_ordering(array: list) -> list:
    # Inicializamos un array vacio para numeros y otro para cadenas
    num_list = []
    string_list = []
    # Llenamos los arrays con cada item de la lista que le pasamos a la funcion en base a su tipo de dato
    for item in array :
        if type(item) != str:
            num_list.append(item)
        else:
            string_list.append(item)
    # Ordenamos ambas listas con .sort() de manera ascendente
    num_list.sort()
    string_list.sort()
    # Concatenamos y retornamos el resultado de ambas listas ordenadas
    sorted_array = num_list + string_list
    return sorted_array

# Ejercicio 8
# Función para ordenamiento MERGE SORT
def merge_sort(arr):
    if len(arr) > 1:
        # Dividir la lista en dos mitades
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llamada recursiva para ordenar ambas mitades
        merge_sort(left_half)
        merge_sort(right_half)

        # Fusionar las dos mitades ordenadas
        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


def insertion_sort_large(to_order):
    for i in range(1, len(to_order)):
        key = to_order[i]  
        j = i - 1  

        while j >= 0 and len(key) < len(to_order[j]):
            to_order[j + 1] = to_order[j]
            j -= 1

        to_order[j + 1] = key
    return to_order

num_list = [5,8,9,3,1,4,5,8,7,5,5,185,5,15,16,5163,4658,463,516,84]

# Llamamos a merge_sort directamente
merge_sort(num_list)
print(num_list)
