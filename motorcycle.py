#24/10/23

from clase_motor import Motorcycle

Moto1 = Motorcycle("rojo","A113",10,2,"Ducatti","Europe",2023,170,90)
Moto2 = Motorcycle("negro","A114", 10,2,"Vespa","Italia",2023,100,60)

Moto1.price = 11000
print(f"La moto Moto 1 {Moto1.marca}, modelo {Moto1.modelo} cuesta : {Moto1.price} $")
Moto1.stop()
Moto1.start()
#print(f"La moto modelo {Moto2.modelo}, año: {Moto2.fabrication_date}, cuesta: {Moto2.price}")

while True:
    try:
        consult = int(input("Si desea consultar el precio de la moto 1 ingrese [1], si desea consultar el precio de la moto 2, ingrese [2]: "))
        if (consult == 1) or (consult == 2):
            break
    except:
        print("Error de entrada. Reintente")

if consult == 1:
    Moto1.price1()
else:
    Moto2.price1()
