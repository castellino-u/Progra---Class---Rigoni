#Ejercicio 1
ano_pc = int(input("Ingrese los años de su computador: "))
if ano_pc <= 2:
    print("Su computador es nuevo")
else: 
    print("Su computador es viejo")    
#Ejercicio 2
ano_pc = int(input("Ingrese los años de su computador: "))
if (ano_pc <= 2) and (ano_pc >= 0) :
    print("su pc es nueva")
elif ano_pc < 0:
    print("error ")
else: 
    print("Su computador es viejo")  

#Ejercicio 16
a= int(input("Ingrese un numero entero: "))
b=int(input("Ingrese otro valor: "))
print("Ingrese la operacion que desea realizar, 1: para suma; 2: para el producto; 3: para la resta; 4: para ver la division")
operacion = (int(input()))
if operacion == 1:
   print(a +b)
elif operacion == 2:
    print(a * b)
elif operacion == 3:
    print(a - b)
elif operacion == 4:
    print(a / b)
else:
   print("Error ") 
#Ejercio 20
nota_1 = int(input("Ingrese la primer nota en una escala del 1 al 10: "))
nota_2 = int(input("Ingrese la segunda nota en una escala del 1 al 10: "))
nota_3 =int(input("Ingrese la tercer nota en una escala del 1 al 10: "))
nota_4 = int(input("Ingrese la cuarta nota en una escala del 1 al 10: "))
promedio = ((nota_1 + nota_2 + nota_3 + nota_4) / 4)
if promedio >= 6:
    print("Aprobado ")
else: 
    print("Desaprobado")