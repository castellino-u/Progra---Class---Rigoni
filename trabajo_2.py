#Correccion del tp 2 
#Ejercicio 1
year_pc = int(input("Ingrese los años de su computador: "))
if year_pc <= 2:
    print("Su computador es nuevo")
else:
    print("Su computador es viejo")    

#Ejercicio 2
year_pc = int(input("Ingrese los años de su computador: "))
if year_pc < 0:
    print("error ")
elif (year_pc <= 2) and (year_pc >= 0) :
    print("su pc es nueva")
else:
    print("Su computador es viejo")  


#Ejercicio 3

nombres=input("ingrese ambos nombres separados:  ")
nombres_separados=nombres.split(" ")
nombre1=nombres_separados[0].lower()
nombre2 = nombres_separados[1].lower()


if (nombre1[0] == nombre2[0]):
  print("Hay concidencia. ")
else:
  print("No hay concidencia. ")


#Ejercicio 4

print("-Elecciones 2023-")
print("Seleccione: ")
print("[A] para el partido AZUL ")
print("[B] para el partido VERDAD ")
print("[C] para el partido ROJO ")
voto = input("Ingrese a que candidato va a votar: ")
voto = voto.upper()
if voto == "A":
    print("Usted a ingresado: ", voto)
    print("Usted a votado por el partido ROJO")
elif voto == "B":
    print("Usted a ingresado: ", voto)
    print("Usted a votado por el partido VERDAD")
elif voto == "C":
    print("Usted a ingresado: ", voto)
    print("Usted a votado por el partido AZUL")
else:
    print("Opción erronea")



#Ejercicio 5


letra = input('Ingresa un caracter: \n')
vocales = ('a','e','i','o','u')
if(len(letra) > 1):
   print('Error de entrada, ingresar solo un carácter')
else:
  if(letra in vocales):
    print(f'La letra "{letra}" es una vocal')




#Ejercicio 6


año = int(input("Ingresar año: "))
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
  print("Año bisiesto")
else:
  print("Año no bisiesto")


#Ejercicio 7:

print("Ingresar tres números")
a = int(input("a= "))
b = int(input("b= "))
c = int(input("c= "))
min = a
if b< min:
    min = b
if c<min:
    min=c
print(f"El número mas pequeño es {min}")


#Ejercicio 8


user = input("Ingrese su usuario: ")
password = input("Ingrese su contraseña: ")

if ((user == "Gwenevere") and (password == "excalibur")):
    print("Usuario y contraseña correctos. Puede ingresar a Camelot")
else:
    print("Acceso denegado")


#Ejercicio 9


nombre = input('Ingresa tu nombre: ')
nombre = nombre.lower()
sexo = input('Ingresa tu sexo (Masculino/Femenino): ')
sexo = sexo.lower()
if(sexo ==  'femenino' or sexo == 'masculino'):
   
  if((sexo == 'femenino') and (nombre[0]< 'm') or ((sexo == 'masculino') and (nombre[0] > 'N'))):
   print('Perteneces al grupo A')
  else:
     print('Perteneces algrupo B')
else:
   print('Error de entrada')


#Ejercicio 10


edad = int(input('Ingresa tu edad: '))
if(edad < 4):
   print('Entrada gratuita')
elif(edad >= 4 and edad < 18):
   print('Valor de entrada 500$')
elif(edad >= 18):
  print('Valor de entrada 1000$')


#Ejercicio 11


pregunta = input(
  '¿Quieres una pizza vegetariana[1] o no vegetariana[2]?\n (Responder [1 o 2]\n')

if pregunta == '1':
  print('Ingredientes vegetarianos\n [Pimiento(1) , Tofu(2)]')
  ingrediente = input('Ingresa una opcion de ingrediente:\n')
  if(ingrediente == '1'):
    ingrediente_adicional = 'Pimiemto'
    print('La pizza es vegatariana\n')
    print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
  elif(ingrediente == '2'):
    ingrediente_adicional = 'Tofu'
    print('La pizza es vegatariana\n')
    print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
elif pregunta == '2':
  print('Ingredientes no vegetarianos\n [Pepperoni(1) , Jamon(2), Salmon(3)]')
  if(pregunta == '2'):
    ingrediente = input('Ingresa una opcion de ingrediente:\n')
    if(ingrediente == '1'):
      ingrediente_adicional = 'Pepperoni'
      print('La pizza no es vegatariana\n')
      print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
    elif(ingrediente == '2'):
      ingrediente_adicional = 'Jamon'
      print('La pizza no es vegatariana\n')
      print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
    elif(ingrediente == '3'):
      ingrediente_adicional = 'Salmon'
      print('La pizza no es vegatariana\n')
      print(f'Y sus ingredientes son Mozzarella, Tomate y {ingrediente_adicional}')
else:
  print('Error de entrada')  


#Ejercicio 12:
fecha_actual = int(input("ingrese la fecha actual: "))
fecha_aleatoria = int(input("ingrese fecha aleatoria: "))
if (fecha_actual > fecha_aleatoria):
  print("Pasaron ",fecha_actual-fecha_aleatoria," años desde esa fecha")
else:
  print("Faltan",fecha_aleatoria-fecha_actual," años para esa fecha")

#Ejercicio 13

num1=int(input('Ingresar numero='))
num2=int(input('Ingresar otro numero='))
if num1>0 and num2>0:
  if num1>num2:
    if num1%num2==0:
      print(f'{num1} es multiplo de {num2}')
    else:
      print(f'{num1} NO es multiplo de {num2}')
  if num2>num1:
    if num1%num2==0:
      print(f'{num2} es multiplo de {num1}')
    else: 
      print(f'{num2} NO es multiplo de {num1}')
else:
  print('Se ingresaron numeros negativos o nulos')

#Ejercicio 14

print("Ingresar los coeficientes de una ecuacion de primer grado ax + b = 0")
a=int(input("a: "))
b=int(input("b: "))


if a==0 and b!=0:
  print("No hay solución")
elif a==0 and b== 0 :
  print("infinitas soluciones")
elif a!=0 :
  b=int(b)
  x=-b/a
  print("la solución es x= ", x)


#Ejercicio 15
import math
operacion=input("Desea saber el area de un triangulo(t) o de un circulo(c): ").lower()   #b*a/2
if (operacion == "c"):
  r=int(input("Escriba el radio del circulo: "))
  print("El area del circulo es de: ", math.pi*(r**2))
elif(operacion=="t"):
  h=int(input("Ingrese la altura del triangulo: "))
  b=int(input("Ingrese la base del triangulo: "))
  print("El area del triangulo es de: ", b*h/2)
else:
  print("valor ingresado no valido ")

#Ejercicio 16

operacion = input("Ingrese la operacion que desea realizar, 1: para suma; 2: para el producto; 3: para la resta; 4: para ver la division:\n")
a = int(input("Ingrese un numero entero: "))
b = int(input("Ingrese otro valor: "))
if operacion == '1':
    print(a +b)
elif operacion == '2':
    print(a * b)
elif operacion == '3':
    print(a - b)
elif operacion == '4':
    if (b == 0):
        print("No se puede dividir por cero")
    else:
        print(a / b)
else:
    print("Error ")

#Ejercicio 17

fecha = input("Ingrese el día: ")
fecha = fecha.lower()

if (fecha == "lunes"):
     
 print("Feliz comienzo de Semana")


elif (fecha == "sábado") or (fecha == "domingo"):


        print("Estas en fin de semana")    


elif (fecha == "viernes"):
   
        print("Feliz fin de semana")        


elif(fecha =="martes" or "miércoles"or "jueves"):


        print("Estás a la mitad de la semana")
                       
else:
        print("El día ingresado no es válido")


print("Fin del programa")

#Ejercicio 18

horas_trabajadas=int(input('Ingresar las horas trabajadas en el mes:'))
salario_hora=int(input('Ingresar su salario por hora:'))
if horas_trabajadas>48:
  horas_extras=horas_trabajadas-48
  print(f'Las horas extras trabajadas fueron:{horas_extras}')
  salario_horas_extras=(salario_hora*0.1)+salario_hora
  salario_total=(48*salario_hora) + (horas_extras+salario_horas_extras)
  print(f'Salario total:${salario_total}')
else:
  print(f'No trabajo horas extras. Las horas trabajadas fueron:  {horas_trabajadas}')
  salario_total=horas_trabajadas*salario_hora
  print("El salario total es: ", salario_total)

#Ejercicio 19 

cant_lapiz = int(input("Ingrese la cantidad de lapices a comprar: "))
precio = 60 * cant_lapiz
if cant_lapiz >= 1000:
    precio_final = precio - (precio * 0.7)
else:
    precio_final = precio


print(f"Se debe pagar ${precio_final} por los {cant_lapiz} lapices")

#Ejercicio 20

nota_1 = int(input("Ingrese la primer nota en una escala del 1 al 10: "))
nota_2 = int(input("Ingrese la segunda nota en una escala del 1 al 10: "))
nota_3 =int(input("Ingrese la tercer nota en una escala del 1 al 10: "))
nota_4 = int(input("Ingrese la cuarta nota en una escala del 1 al 10: "))
promedio = ((nota_1 + nota_2 + nota_3 + nota_4) / 4)
if (nota_1 > 0 and nota_1 < 11) and (nota_2 > 0 and nota_2 < 11) and (nota_3 > 0 and nota_3 < 11) and (nota_4 > 0 and nota_4 < 11):
    if promedio >= 6:
        print("Aprobado ")
    else:
        print("Desaprobado")
else: 
    print("Error de entrada de datos")

