#Ejercicio 1-------------------------------------------------------------------
class Persona:
    def __init__(self, name = '', age = 0, DNI = 0) -> None:
        self.name = name
        self.age = age
        self.DNI = DNI



# Definicion de getters
    @property
    def get_name(self):
        return self.name
    @property
    def get_age(self):
        return self.age
    @property
    def get_DNI(self):
        return self.DNI

# Definicion de setters


    def set_name(self, new_name):
        if type(new_name) == str:
            self.name = new_name
        else:
            print('El nombre debe ser una cadena de texto')


    def set_age(self, new_age):
        if type(new_age) == int:
            self.age = new_age
        else:
            print('La edad debe ser un valor entero')


    def set_DNI(self, new_DNI):
        if type(new_DNI) == str:
            self.DNI = new_DNI
        else:
            print('El DNI debe ser un valor entero')


    def mostrar(self):
        print(self.name)
        print(self.age)
        print(self.DNI)


    def es_mayor_edad(self):
        if self.age >= 18:
            return True
        else:
            return False


#Ejercicio 2------------------------------------------------------------------------------------


class Count:


#constructor
    def __init__(self, owner, amount = 0.0):
        self.owner = owner
        self.amount = amount


    #Definicion de getters
    @property
    def get_owner(self):
        return self.owner


    @property
    def get_amount(self):
        return self.amount



#Definiendo setters

    def set_owner(self, new_owner):
        self.owner = new_owner


    def set_amount(self, pre_balance):
        self.amount += pre_balance





    ###   Métodos   ###


    #Mostrar los datos de la cuenta
    def show_info(self):
        print(f"Titular de la cuenta: {self.owner}.\nCantidad: {self.amount}")


    #Ingresar dinero
    def entry_money(self, quanty):
        if quanty >= 0:
            self.amount += quanty
            print(f"Saldo actual: {self.amount}")
        else:
            print("Ingreso de dinero inválido")



    #Retirar dinero
    def withdraw(self, quanty):
        if quanty >= 0:
            self.amount -= quanty
            print(f"Saldo actual: {self.amount}")
        else:
            print("Retiro de dinero inválido")
programa principal
c1 = Count("Thomas Muñoz", 38522.59)


c1.show_info()
c1.set_amount(2000.0)
c1.show_info()
c1.set_amount(-5000.0)
c1.show_info()
c1.entry_money(5)
c1.entry_money(-5)
c1.withdraw(6)
c1.withdraw(-6)

#Ejercicio-3----------------------------------------------------------------

#clase
class Triangle:
    #creamos el constructor de la clase triangulo, donde luego se van a cargar los lados de un triangulo
    def __init__(self,side1,side2,side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    #Esta es la funcion que me va a decir, según sus lados, el tipo de triángulo
    def type_triangle(self):
        #evalua si son todos iguales
        if (self.side1 == self.side2) and (self.side2 == self.side3):
            print("Según sus lados, el triangulo ingresado es un triangulo equilatero.")
        #si no, evalua si son todos distintos
        elif (self.side1 != self.side2) and (self.side2 != self.side3):
            #evalua que el lado 1 sea el mayor
            if (self.side1 > self.side2) and (self.side1 > self.side3):
                print("Según sus lados, el triangulo ingresado es un triangulo escaleno. ")
                print (f"El lado con un mayor tamaño es: {self.side1}")
            #evalua que el lado 2 sea el mayor
            elif (self.side2 > self.side1) and (self.side2 > self.side3):
                print("Según sus lados, el triangulo ingresado es un triangulo escaleno. ")
                print (f"El lado con un mayor tamaño es: {self.side2}")
            #condicion que toma por descarte el lado 3
            else:
                print("Según sus lados, el triangulo ingresado es un triangulo escaleno. ")
                print (f"El lado con un mayor tamaño es: {self.side3}")
        else:
            print("Según sus lados, el triángulo ingresado es un triángulo isósceles ")

#Main
#instancia del objeto triangulo
triangle1 = Triangle(2,3,4)
triangle1.type_triangle()
print("- - - ")
triangle2 = Triangle(4,4,4)
triangle2.type_triangle()
print("- - - ")

triangle3 = Triangle(5,3,3)
triangle3.type_triangle()
print("- - - ")

#Ejercicio--4------------------------------------------------------------------------------------------

## Crear una clase que administre una agenda, por cada contacto almacenar (nombre -> str, telefono -> int y gmail -> str)


class Schedule():
    def __init__(self) -> None:
        self.contacts = []

    def add_contact(self, name, phone, gmail):
        contact = {
            'name': name,
            'phone': phone,
            'gmail': gmail
        }
        self.contacts.append(contact)
    def show_contacts(self):
        if len(self.contacts) != 0:
            for contact in self.contacts:
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Gmail: {contact['gmail']}")
                print()
        else:
            print('No tienes contactos para mostrar.')
    def search_contacts(self, to_search):
        contact_found = False
        for contact in self.contacts:
            if to_search.lower() == contact['name'].lower():
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Gmail: {contact['gmail']}")
                contact_found = True
        if not contact_found:
            print('El contacto no existe')
    def edit_contact(self, to_edit, new_name, new_phone, new_gmail):
        contact_found = False
        for contact in self.contacts:
            if to_edit.lower() == contact['name'].lower():
                contact['name'] = new_name
                contact['phone'] = new_phone
                contact['gmail'] = new_gmail
                print('Contacto editado con éxito')
                contact_found = True
        if not contact_found:
            print('El contacto no existe')

# Main
schedule = Schedule()


while True:
    print('Bienvenido al menu de tu agenda, que quieres hacer?\n[1] Añadir contacto\n[2] Lista de contactos\n[3] Buscar contacto\n[4] Editar contacto\n[5] Cerrar agenda')
    op = input('Ingresa una opción valida: ')
    if op == '1':
        print('Crear contacto\n')
        name = input('Ingresa el nombre del nuevo contacto: ')
        phone = int(input('Ingresa el telefono del nuevo contacto: '))
        gmail = input('Ingresa el gmail del nuevo contacto: ')
        schedule.add_contact(name,phone,gmail)
        print('Contacto añadido')
    elif op == '2':
        print('Ver lista de contactos')
        schedule.show_contacts()
    elif op == '3':
        to_search = input('Ingresa el nombre del contacto que quieres buscar: ')
    elif op == '4':
        to_edit = input('Ingresa el nombre del contacto que deseas editar: ')
        new_name = input('Nuevo nombre: ')
        new_phone = int(input('Nuevo teléfono: '))
        new_gmail = input('Nuevo correo electrónico: ')
        schedule.edit_contact(to_edit, new_name, new_phone, new_gmail)
        schedule.search_contacts(to_search)
    elif op == '5':
        print('Cerrando agenda')
        break


#Contactos
class Contacts:


    def __init__(self, contact_list = []):
        self.contact_list = contact_list



#Main
import aFunciones as funcion
from Contactos import Contacts

c1 = Contacts([["Thomas Muñoz", 2616978762, "aaa@gmail.com"]])


option = 1
while option != 0:
    print(f"\n¿Que desea ralizar? \nAñadir Contacto(1) \nVer lista de contactos(2) \nBuscar contacto(3) \nEditar Contacto(4) \nCerrar agenda(0)")


    option = funcion.valid_int("Ingrese una opcion: ")
    #Menú
    if option == 1:
        c1.contact_list.append(funcion.new_contact())
    if option == 2:
        for i in range(0, len(c1.contact_list)):
            print(f"Contacto {i+1}:\n  Nombre:{c1.contact_list[i][0]}.\n  Número de teléfono: {c1.contact_list[i][1]}.\n  Email: {c1.contact_list[i][2]}")
    if option == 3:
        print("Busqueda por nombre")
        search = input("Ingrese el nombre del contacto: ").title()
        coincidence = 0
        contact = 0
        for i in range(0, len(c1.contact_list)):


            if search == c1.contact_list[i][0]:
                coincidence += 1
                contact = i + 1




        if coincidence == 1:
            print(f"Se encontró el contacto. Es el número {contact}")
        else:
            print("No se encontró el contacto")
    if option == 4:
        edit = funcion.valid_int("Ingrese el contacto a editar: ")-1
        if edit < len(c1.contact_list):
            print("Que desea editar? \n Nombre(1) \n Número(2) \n Email(3)")
            edit_option = funcion.valid_int("Ingrese una opción: ")
            if edit_option == 1:
                c1.contact_list[edit][0] = input("Ingrese el Nombre: ")

            elif edit_option == 2:
                c1.contact_list[edit][1] = funcion.valid_int("Ingrese el Nombre: ")

            elif edit_option == 3:
                while True:
                    email = input("Ingrese el email: ")
                    if "@" in email and "." in email:
                        c1.contact_list[edit][3] = email
                        break
                    else:
                        print("Ingrese una direccion de email válida")
            else:
                print("Opción inválida")
print("Saliendo...")

funciones
### Funciones TP 9 ###
def valid_int(promp):
    while True:
        try:
            entry = int(input(f"{promp}"))
            return entry
        except ValueError:
            print("Ingrese un número")


def new_contact():
    name = input("Ingrese el nombre del contacto: ").title()
    num = valid_int("Ingrese el número de telefono: ")
    while True:
        email = input("Ingrese el email: ")
        if "@" in email and "." in email:
            return([name, num, email])
        else:
            print("Ingrese una direccion de email válida")




