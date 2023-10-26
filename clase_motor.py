#en python constructor hay uno solo
#para crear un constructor vacio hago esto
#def __init__(sefl, name = "", age = 0):
#el self es como "esta"
class Motorcycle:
    state = "0km"
    engine = False
    #este def es para crear el constructor del objeto. Nos permite aignar atributos y realizar operaciones con el objeto
    def __init__(self,color,number_plate,fuel_liter,number_wheels,marca,modelo,fabrication_date,top_speed,weight):
        #lo que hacemos ahora escrear el constructor
        #el self es como el this, se usa para representar una instancia actual de la clase.
        self.color = color
        self.number_plate = number_plate
        self.fuel_liter = fuel_liter
        self.number_wheels = number_wheels
        self.marca = marca
        self.modelo = modelo
        self.fabrication_date = fabrication_date
        self.top_speed = top_speed
        self.weight = weight

    def start(self):
        
        if (self.engine == False):
            self.engine = True
            print("El motor ha arrancado")
        else:
            print("El motor ya esta en marcha")

    def stop(self):
        if (self.engine == True):
            self.engine = False
            print("El motor se ha detenido")
        else:
            print("El motor ya estaba detenido")

    def price1(self):
        print(f"El precio de la moto es: {self.price}")

#Bien, hasta aca esta todo bien, la clase ya esta creada y terminar y dejar este archiv aca
#puedo instanciar(crear) un objeto aca fuera de la clase obviamente o bien puedo crear otro archivo
#y crear o instanciar el objeto en ese otro archivo. Atencion, si hago esto, al igual que las funcionescreadas en otro archivo, debo
#importar la clase



