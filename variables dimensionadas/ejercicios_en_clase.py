#ejercicio 1
import funciones 
passenger_data=[('Paula Geier', 44593085, 'Rio De Janeiro'), ('Rodrigo Zapata', 47805624, 'Cordoba'),('Thomas Muñoz', 94219667, 'Vancuver')]
country_belonging=[('Brasil','Rio De Janeiro'),('Argentina','Cordoba'),('Canada','Vancuver'),('Brasil','Bahia')]
salida=False
while salida==False:
    print('MENU\n1.Agregar pasajeros a la lista de viajeros\n2.Agregar ciudades a la lista de ciudades\n3.Dado el DNI de un pasajero, ver a qué ciudad viaja\n4.Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad\n5.Dado el DNI de un pasajero, ver a qué país viaja\n6.Dado un país, mostrar cuántos pasajeros viajan a ese país\n7.Salir del programa')
    option=int((input("Ingresar el NUMERO de opcion:")))
    if option==1:
        new_name=input("Nombre y apellido del pasajero:")
        new_dni=int(input("DNI del pasajero:"))
        new_city=input('Ciudad de destino:')
        new_country=input("Pais de destino:")
        passenger_data.append((new_name,new_dni,new_city))
        country_belonging.append((new_country,new_city))
        #Agregar pasar las primeras letras en mayusculas y el resto en minuscula
        print(f"Nuevo pasajero:{(passenger_data[-1])[1]}")
        print(f"DNI:{(passenger_data[-1])[0]}")
        print(f"Ciudad de destino:{(passenger_data[-1])[2]}")
    elif option==2:
        print("Ciudades existentes:")
        for n in range(len(country_belonging)):
            print(f"{n+1}_{(country_belonging[n])[0]},{(country_belonging[n])[1]} ")
        new_city=input('Ingresar ciudad nueva:')
        new_country=input('Ingresar pais de la ciudad:')
        country_belonging.append((new_city,new_country))
        print("Ciudad agregada")
    elif option==3:
        search_dni=int(input('Ingresar el DNI del pasajero:'))
        for n in range(len(passenger_data)):
            if search_dni in passenger_data[n]:
                print(f"{(passenger_data[n])[0]} viaja con destino a {(passenger_data[n])[2]}")
    elif option==4:
        number_of_passengers=0
        print("Seleccionar el numero de la ciudad:")
        for n in range(len(country_belonging)):
            print(f"{n+1}_{(country_belonging[n])[0]},{(country_belonging[n])[1]}")
        chosen_city=int(input())
        for n in range(len(passenger_data)):
            if (country_belonging[chosen_city-1][1]) in passenger_data[n]:
                number_of_passengers+=1
        print(f"Cantidad de pasajeros que viajan a {country_belonging[chosen_city-1]}: {number_of_passengers}")
    elif option==5:
        search_dni=int(input('Ingresar el DNI del pasajero:'))
        for n in range(len(passenger_data)):
            if search_dni in passenger_data[n]:
                destination_city=(passenger_data[n])[2]
                for n in range(len(country_belonging)):
                    if destination_city in country_belonging[n]:
                        print(f"{(passenger_data[n])[0]} viaja con destino a {(country_belonging[n])[0]}")
    elif option==6: 
        number_of_passengers=0
        print("Seleccionar el numero del pais:")
        for n in range(len(country_belonging)):
            print(f"{n+1}_{(country_belonging[n])[0]}")
            #Hacer una sola lista de paises sin que estos se repitan si hay mas de un pasajero que viaja alli
        chosen_country=input()
        for c in country_belonging:
            if chosen_country==c[0]:
                ax=c[1]
                for p in passenger_data:
                    if ax==p[2]:
                        number_of_passengers+=1
        print(f"Los pasajeros que viajan a {chosen_country} son: {number_of_passengers}")
    elif option==7:
        print("VUELVA PRONTO :)")
        break

#Ejercicio 2
import funciones
shopping=[('Nuria Costa', 5, 1234.5,'Calle 1 - 456'), ('Jorge Russo', 7, 3999, 'Calle 2 - 741'),('Paula Geier', 10, 954, 'Calle 6 - 985'),('Nuria Costa', 25, 3569,'Calle 1 - 456'),('Marta Rolon', 30, 3524,'Calle 7 - 653')]

print("DOMICILIOS")
for n in range(len(funciones.addresses(shopping))):
    print(f"{(funciones.clients(shopping))[n]} - {(funciones.addresses(shopping))[n]}")

#Ejercicio 3

partners={
    'Socio n°1':{
        'nombre':' Amanda Núñez',
        'ingreso':'17/03/2009',
        'estado_cuota':'al dia'
    },
    'Socio n°2':{
        'nombre':'Bárbara Molina',
        'ingreso':'17/03/2009',
        'estado_cuota':'al dia'
    },
    'Socio n°3':{
        'nombre':'Lautaro Campos',
        'ingreso':'17/03/20092',
        'estado_cuota':'al dia'
    }
}
option=0
while option!=7:

    print("MENU")
    print("1.Cargar informacion de los socios\n2.Cantidad de socios del club\n3.Registrar pago de cuotas\n4.Modificar fecha de ingreso de socios(ingresados el  13/03/2018, cambiar fecha al 14/03/2018) \n5.Eliminar socio\n6.Listado de socios\n7.Salir del programa")
    option=int(input("Ingresar el numero de la opcion que desea realizar: "))
    if option==1:    
        clue_dictionary=f'Socio n°{len(partners)+1}'
        partners[clue_dictionary]={}
        partners[clue_dictionary]['nombre']=input("Ingresar nombre y apellido del socio: ")
        partners[clue_dictionary]['ingreso']=input("Ingresar fecha de ingreso del socio (dd/mm/aaaa): ")
        partners[clue_dictionary]['estado_cuota']=input("Ingresar estado de la cuota del socio(adeuda/al dia): ") 
        print("Socio ingresado con exito!")
    elif option==2:
        print(f'La cantidad de socios son: {len(partners)}')
    elif option==3:
        membership_number=int(input("Ingresar el numero de socio: "))
        partners[f'Socio n°{membership_number}']['estado_cuota']='al dia'
        print(f'El socio n°{membership_number} ahora registra tiene sus cuotas al dia')
    elif option==4:
        for clue in range(len(partners)):
            if partners[f'Socio n°{clue}']['ingreso']=='13/03/2018':
                partners[f'Socio n°{clue}']['ingreso']='14/03/2018'
    elif option==5:
        partner_to_eliminate=input("Ingresar el numero  de socio que desea eliminar: ")
        del partners[f'Socio n°{partner_to_eliminate}']
        print(f'Socio n°{partner_to_eliminate} eliminado')
    elif option==6:
        for clave, socio in partners.items():
            print(f"-{clave},{socio['nombre']}, ingreso {socio['ingreso']}, cuota {socio['estado_cuota']}")
    elif option==7:
        print("Programa cerrado")

