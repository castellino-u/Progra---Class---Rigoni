import random

def find_word(random_word, board, attempts, letter):
    if letter in random_word:  # Si la letra está en la palabra
        print("Adivinaste una letra correctamente")
        for i in range(len(random_word)):
            if random_word[i] == letter:  # Si la letra es correcta, actualiza el tablero
                board[i] = letter
    else:  # Si la letra es incorrecta
        attempts -= 1  # Resta un intento
        print(f"Letra incorrecta, te quedan {attempts} intentos")
    return attempts

# Lista de palabras
words = ['programacion', 'python', 'computacion', 'java', 'tecnologia', 'utn', 'mendoza', 'argentina', 'pablo', 'laboratorio']
random_word = random.choice(words)  # Se elige una palabra aleatoria

board = ["_" for _ in random_word]  # Crea un tablero con guiones bajos para cada letra de la palabra
attempts = 6  # Número de intentos permitidos

while attempts > 0:
    if all(letter in random_word for letter in board):  # Si todas las letras han sido adivinadas
        break
    print(" ".join(board))  # Imprime el estado actual del tablero
    letter = input("Ingresa una letra: ")  # Usuario ingresa una letra
    letter = letter.lower()  # Convierte la letra a minúsculas
    
    if len(letter) != 1 or not letter.isalpha():  # Validación de entrada
        print("Ingresa una sola letra y que sea valida")
        continue
    
    attempts = find_word(random_word, board, attempts, letter)  # Comprueba si la letra es correcta

if "_" not in board:  # Si no hay guiones bajos en el tablero, todas las letras fueron adivinadas
    print(f"¡¡¡Felicidades!!! adivinaste la palabra '{random_word}'")
else:
    print(f"Mala suerte, no pudiste adivinar la palabra, la palabra era '{random_word}'")  # Mensaje si no se adivina la palabra
