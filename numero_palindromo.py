import os
import time

#
#   funcion para limpiar la consola
#
def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

#
#   funcion para verificar si un numero es palindromo
#
def es_palindromo(n: int) -> bool:
    if n < 0:
        return False
    
    original = n
    reverso = 0

    while n > 0:
        reverso = reverso * 10 + n % 10
        n //= 10
    
    return original == reverso

def verificar_numero():
    try:
        limpiar_consola()
        numero = int(input("Introduce un número entero: "))
        if es_palindromo(numero):
            print(f"El número {numero} es un palíndromo.")
        else:
            print(f"El número {numero} no es un palíndromo.")
        time.sleep(3)
    except ValueError:
        print('debe ingresar un numero entero')
        time.sleep(2)

#
#   funcion para verificar si un numero es palindromo en un rango de numeros
#
def comprobar_rango():
    try:
        limpiar_consola()
        x = int(input("Introduce el numero inicial del rango: "))
        y = int(input("Introduce el numero final del rango: "))
        for numero in range(x, y + 1):
            if es_palindromo(numero):
                print(f"El número {numero} es un palíndromo.")
            else:
                print(f"El número {numero} no es un palíndromo.")
        time.sleep(5)
    except ValueError:
        print('debe ingresar un rango valido')
        time.sleep(2)

#
#   funcion para mostrar el menu
#
def menu():
    while True:
        limpiar_consola()
        print('Bienvenido al programa de palindromos')
        print('1. Verificar un numero si es palindromo')
        print('2. Verificar un rango de numeros si son palindromos')
        print('3. Salir del programa')

        try:
            opcion = int(input('Ingrese una opcion: '))
            if opcion == 1:
                verificar_numero()
            elif opcion == 2:
                comprobar_rango()
            elif opcion == 3:
                print('Gracias por usar el programa, saliendo del programa')
                time.sleep(1)
                break
            else:
                print('Opcion invalida, intente nuevamente')
                time.sleep(2)
        except ValueError:
            print('debe ingresar un numero entero')
            time.sleep(2)
        except KeyboardInterrupt:
            print('Saliendo del programa')
            time.sleep(1)
            break
    limpiar_consola()
#
#   ejecutar el menu
#
menu()