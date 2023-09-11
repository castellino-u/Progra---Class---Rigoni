fecha = (input("Ingrese la fecha en formato dia(dia de la semana) \n Ingrese coma, ingrese un espacio;\n el numero del dia, barra, el numero del mes: "))
#print(fecha)
dia_sem= fecha[0:fecha.find(",")]

num_dia = fecha[fecha.find(" ")+1:fecha.find("/")]
num_dia = int(num_dia)

mes = fecha[fecha.find("/")+1:]
mes = int(mes)

dia_sem= dia_sem.lower()
#print(dia_sem)
dias_sem_tupla= ("lunes","martes","miercoles","jueves","viernes")
if (dia_sem in dias_sem_tupla): 
    if (num_dia >0) and (num_dia < 32):
        if (mes > 0) and (mes < 13):
            if (dia_sem =="lunes") or (dia_sem == "martes") or (dia_sem == "miercoles"):
                test= input("¿Hubieron examenes?: Ingrese Si o No. ")
                test = test.lower()
                if test == "si":
                     aprobados= int(input("Ingrese la cantidad de aprobados: "))
                     desaprobados= int(input("Ingrese la cantidad de desaprobados: "))
                     procentaje_aprobados = (aprobados * 100)/ (aprobados + desaprobados)
                     print(" el porcentaje de aprobados es: ",procentaje_aprobados)
            elif dia_sem == "jueves": 
                asistencia = int(input("Ingrese el porcentaje de asistencia a clase: "))   
                if asistencia >= 50:
                    print("Asistio la mayoria")
                else: 
                    print("No asistió la mayoria. ")
            elif dia_sem == "viernes":
                if (mes == 1) or (mes == 7):
                    if dia_sem == 1:
                        print("Nuevo comienzo de ciclo")
                        alum_nuevo_ciclo = int(input("Ingrese la cantidad de alumnos del nuevo ciclo: "))
                        arancel= int(input("Ingrese el arancel por alumno: "))
                        print("El ingreso total es de: ", alum_nuevo_ciclo * arancel)
else:
    print("Error")                       
                                               
