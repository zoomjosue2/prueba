#==========================================================
# Universidad del Valle de Guatemala
# Algoritmos y progra basica
# Seccion 60
# 
# Josué García - 24918
# José Sanchez - 24092
# MEA - Parte 2
# 11/05/24
#==========================================================

import pandas as pd
import matplotlib.pyplot as plt

sismos = pd.read_csv('reporte_sismos_2019_2023.csv')

#1
def ultimos_sismos ():
    numero_sismos = len(sismos)
    return numero_sismos
#2
def sismos_n (n):
    sismos_n1 = sismos.loc[sismos["Anio"] == n]
    cantidad_ano = len(sismos_n1)
    return cantidad_ano
#3
def numero10 (n):
    sismos_n2 = sismos.loc[sismos['Anio'] == n]
    cantidad_ano2 = sismos_n2.head(10)
    return cantidad_ano2
#4
def sismos_demenor (n):
    sismos_n3 = sismos.sort_values('MAG', ascending=True)
    cantidad_ano3 = sismos_n3.head(n)
    return cantidad_ano3
#5
def sismos_estaciones (n):
    sismos_n4 = sismos.loc[sismos['Anio'] == n]
    cantidad_ano4 = sismos_n4.sort_values('NST', ascending=True).head(10)
    return cantidad_ano4
#6
def magnitud_promedio (n):
    sismos_n5 = sismos.loc[sismos['Anio'] == n]
    cantidad_ano5 = sismos_n5['MAG'].mean()
    return cantidad_ano5
#7
def magnitud_profundidad ():
    sismos["TiempodeOrigen"] = pd.to_datetime(sismos["TiempodeOrigen"])
    sismos["Mes"] = sismos["TiempodeOrigen"].dt.month

    promedio_magnitud = sismos.groupby("Mes")["MAG"].mean()
    promedio_profundidad = sismos.groupby("Mes")["Profundidad"].mean()

    print("Magnitud promedio por mes: \n", promedio_magnitud)
    print("Profundidad promedio por mes: \n", promedio_profundidad)

    opcion_grafica = input("¿Qué gráfica desea ver? 1. Magnitud - 2. Profundidad: ")

    if opcion_grafica == "1":
        promedio_magnitud.plot(kind="bar", title="Promedio de magnitud por mes", grid=True, stacked=False, rot=0)
        plt.xlabel("Mes")
        plt.ylabel("Magnitud promedio")
        plt.show()
        

    elif opcion_grafica == "2":
        promedio_profundidad.plot(kind="bar", title="Promedio de profundidad por mes", grid=True, stacked=False, rot=0)
        plt.xlabel("Mes")
        plt.ylabel("Profundidad promedio en KM")
        plt.show()
    else:
        print("Ingrese una opción válida")

#8
def sismos_sensibles ():
    total = sismos.groupby('Anio')['Sensible'].size()
    print(total)

    #total_si = sismos[sismos['Sensible'] == "si"].size
    #print(total_si)


    sismos_sensibles = sismos[sismos['Sensible'] == "si"].groupby('Anio').size()
    
    #promedio_sensibles = sismos_sensibles.to_numeric.to_numeric().mean()
    #promedio_sensibles = sismos_sensibles.groupby("Anio").size().mean()
    
    #opcion_grafica = input("¿Desea ver la gráfica? 1. Sí - 2. No: ")
    #if opcion_grafica == "1":
     #   sismos_sensibles.groupby("Anio").size().plot(kind="bar", title="Sismos sensibles por año", grid=True, stacked=False, rot=0)
      #  plt.xlabel("Año")
       # plt.ylabel("Cantidad de sismos sensibles")
       # plt.show()
    #elif opcion_grafica == "2":
     #   print("No se mostrará una gráfica")
    #else:
     #   print("Ingrese una opción válida")

    return sismos_sensibles
#9
def error ():
    sismos_error = sismos[sismos['No'].str.contains("*",regex=False)]
    sismos_error_por_ano = sismos_error.groupby("Anio").size()

    return sismos_error_por_ano

#10
def fases ():
    cantidad_ano10 = sismos.sort_values('NF', ascending=True).head(3)
    return cantidad_ano10 


opcion = ""
while opcion != "11":
    print("""Estas son las opciones disponibles
    (1) Cantidad de sismos en los últimos años
    (2) Cantidad de sismos durante un año en especifico
    (3) Primeros 10 sismos que ocurrieron durante un año en especificos
    (4) Los sismos con menor intensidad
    (5) Los 10 sismos que fueron detectados por la menor cantidad de estaciones
    (6) Magnitud promedio de un año en especifico
    (7) Magnitud y profundidad promedio de los sismos por un mes en especifico
    (8) Cantidad de sismos sensibles que han ocurrido en promedio por año
    (9) Cantidad de sismos que tienen un error mayor a 25 kms en su localización por año
    (10) Información del sismo que ha tenido la menor cantidad de fases
    (11) Salir""")
    opcion = input("\nElige la opción deseada colocando el número de lo que se desea ejecutar en el programa: ")
    if opcion == "1":
        print(f"\nLa cantidad de sismos que han ocurrido los ultimos 5 años: {ultimos_sismos()}\n")
        print(f"Las columnas de nuestra DataFrame son:\n{sismos.columns}")

    elif opcion == "2":
        n = int(input("Ingrese el año deseado: "))
        print(f"\nLa cantidad de sismos en {n} fue de: {sismos_n(n)}\n")

    elif opcion == "3":
        n = int(input("Ingrese el año deseado: "))
        print(f"\n Los 10 primeros sismos ocurridos en {n} fueron: \n{numero10(n)}")

    elif opcion == "4":
        n = int(input("Ingrese la cantidad de sismos que quiere ver: "))
        print(f"\nLos {n} sismos con menor intensidad son: \n{sismos_demenor(n)}\n")

    elif opcion == "5":
        n = int(input("Ingrese el año deseado: "))
        print(f"\nLos 10 sismos que fueron detectados por el menor número de estaciones en {n} fueron: \n{sismos_estaciones(n)}\n")
    
    elif opcion == "6":
        n = int(input("Ingrese el año deseado: "))
        print(f"\nEl promedio de la magnitud en el año {n} es: {magnitud_promedio(n)}")
    
    elif opcion == "7":
        magnitud_profundidad()

    elif opcion == "8":
        print(f"\nPromedio de los sismos sensibles: {sismos_sensibles()}\n")
        
    elif opcion == "9":
        print(f"\nSismos con un error mayor a 25kms en su localización por año: \n{error()}\n")
    
    elif opcion == "10":
        print(f"\nInformación de los sismos que han tenido la menor cantidad de fases: \n{fases()}\n")
    
    elif opcion == "11":
        print("\nEl programa ha terminado\n")
    
    else: 
        print("\nElija una opción válida\n")