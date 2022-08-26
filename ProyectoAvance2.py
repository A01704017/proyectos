""" Avance 2 del Proyecto
Programa para el aprendizaje del idioma Alemán
En este programa implemente el uso de variables, tipos y operadores."""

#Este es el quiz de numeros donde se evaluaran los conocimientos. 
def quiznum():
    #Este contador contara las respuestas correctas del usuario. Para esto utilice operadores. 
    count = 0
    
    p1 = str(input("Escribe el numero 1 en alemán: "))
    if p1 == "eins":
        count += 1
    else:
        count += 0
        
    p2 = str(input("Escribe el numero 2 en alemán: "))
    if p2 == "zwei":
        count += 1
    else:
        count += 0
    
    print("Puntaje final: ",count)
    #Después aquí implementare opción para volver al menu principal o salir. 
    

#Esta es la sección para que el usuario aprenda sobre los numeros en alemán
#En el siguiente avance aumentare la información 
def numeros():
    print("\n Esta es la seccion de numeros, donde aprenderas a contar en aleman")
    print("\n Comencemos contando del 1 al 10:")
    print(" 1- eins  2- zwei  3- drei  4- vier  5- fünf  6- sechs  7- sieben  8- acht  9- neun  10- zehn")
    print("\n")
    #Después de presentarle al usuario la información, tendra la opción de hacer un quiz para corroborar su aprendizaje.
    quiz = str(input("¿Estas listo para ir al quiz? \n Escribe'si' para ir al quiz y 'no' para volver al menu: "))
    if quiz == "si":
        #El usuario es dirigido al quiz. 
        n_quiz = quiznum()
    else:
        #El usuario es dirigido al menu principal.
        menu_principal = menu()

#Imprime el menu de opciones al usuario. 
def menu():
    print("\n Bienvenido, selecciona la opcion para aprender el día de hoy escribiendo el numero.\n")
    print("1. Los números")
    print("0. Salir del programa")

#Este es el menu principal, dónde el usuario elige la sección que quiere aprender. 
def main():
    inicio = menu()
    opcion = str(input("Ingresa la opción: "))
    if opcion == "1":
        snumeros = numeros()
    elif opcion == "0":
        quit()
        
main()