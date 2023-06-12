import os
import time
import numpy as np
import funciones_medicas as fm

# --------------- Variables -----------------
opcion = ""
tamaño = 2
rut = ""
arr_rut = np.empty(tamaño, dtype=object)
nombre = ""
arr_nombres = np.empty(tamaño, dtype=object)
edad = 0
arr_edades = np.empty(tamaño, dtype=object)
# ------------- Codigo principal -------------
while True:
    os.system("cls")
    opcion = str(
        input(
            """
    --------- MENÚ ----------
    1.- Ingresar datos
    2-. Busqueda por rut
    3.- Imprimir Ficha
    4.- Salir                   
    \nElija opción:  """
        )
    )

    if opcion == "1":
        os.system("cls")
        rut = str(input("Ingrese rut: "))
        while not fm.validar_rut(rut):
            print("Error rut invalido")
            rut = str(input("Ingrese rut: "))

        nombre = str(input("Ingrese nombre: "))
        while not fm.validar_nombre(nombre):
            print("Error nombre debe tener mas de 3 caracteres")
            nombre = str(input("Ingrese nombre: "))

        edad = int(input("Ingrese edad: "))
        while not fm.validar_edad(edad):
            print("Edad invalida")
            edad = int(input("Ingrese edad: "))

        os.system("pause")

    if opcion == "2":
        os.system("cls")

        os.system("pause")

    if opcion == "3":
        os.system("cls")

        os.system("pause")

    if opcion == "4":
        os.system("cls")
        print("...cerrando app")
        time.sleep(1)
        break
