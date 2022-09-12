"""Esta función contiene una actividad de practica con ejercicios para repasar los articulos.
Utiliza condicionales y operadores para sumar los puntos obtenidos en el quiz y después
enviarlos a la función del promedio para que el usuario vea su puntaje total."""
def practica_articulos():
    count = 0
    print("Escribe el articulo correspondiente para cada palabra.\nTendras tres oportunidades para sacar bien la respuesta.\nObtendras el punto solo si la respuesta es correcta en el primer intento.")
    
    for cont1 in range (0,3):
        p1 = str(input("Haus, der die das: "))
        if p1 == "das":
            count += 1
            break
        else:
            if cont1 < 2:
                print("Intentalo de nuevo")
            else:
                print("La respuesta correcta es 'das'.")
                continue

    for cont2 in range (0,3):
        p2 = str(input("Computer, der die das: "))
        if p2 == "der":
            count += 1
            break
        else:
            if cont2 < 2:
                print("Intentalo de nuevo")
            else:
                print("La respuesta correcta es 'der'.")
                continue
            
    for cont3 in range (0,3):
        p3 = str(input("Mann, der die das: "))
        if p3 == "der":
            count += 1
            break
        else:
            if cont3 < 2:
                print("Intentalo de nuevo")
            else:
                print("La respuesta correcta es 'der'.")
                continue
            
    for cont4 in range (0,3):
        p4 = str(input("Sonne, der die das: "))
        if p4 == "die":
            count += 1
            break
        else:
            if cont4 < 2:
                print("Intentalo de nuevo")
            else:
                print("La respuesta correcta es 'die'.")
                continue
            
    for cont5 in range (0,3):
        p5 = str(input("Mädchen, der die das: "))
        if p5 == "das":
            count += 1
            break
        else:
            if cont5 < 2:
                print("Intentalo de nuevo")
            else:
                print("La respuesta correcta es 'das'.")
                continue
    
    puntaje_total = calculadora(count)
    print("Puntaje total:",puntaje_total)
    
    menu_opciones = str(input("Si deseas volver a la sección anterior teclea ´si´.Para el menú principal teclea 'm´: "))
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            articulos_seccion = articulos()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("Si deseas volver a la sección anterior teclea ´si´.Para el menú principal teclea 'm´: "))
        break
    
"""Esta función se encarga de mostrar la información sobre los articulos en alemán.
Tambén dirige con un condicional al usuario hacia la practica o devuelta la menú."""
def articulos():
    print("\nSe utiliza der para:")
    print("1.Al referirse al género masculino \n2.Con años, semanas y estaciones del año \n3.Sustantivos que terminan en -er, -ant, -ner")
    print("\nSe utiliza die para:")
    print("1.Referirse al género femenino \n2.Sustantivos que terminan en heit, keit, schaft, ung, ade, age, anz, nz, ik, ion, tät, ur, -e , ei, ie y in")
    print("\nSe utiliza das para:")
    print("1.Sustantivos terminan en -chen, -um, -ment, -nis \n2.Colores \n3.Sustantivos que se derivan de infinitivos")
    
    menu_opciones = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea 'm´: "))
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            articulos_actividad = practica_articulos()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea 'm´: "))
        break
    
"""Esta función contiene un quiz con ejercicios para practicar los numeros.
Utiliza condicionales y operadores para sumar los puntos obtenidos en el quiz y después
enviarlos a la función del promedio para que el usuario vea su puntaje total."""
def quiznum():
    count = 0
    
    p1 = str(input("Escribe el número 8 en alemán: "))
    if p1 == "acht":
        count += 1
    else:
        count += 0
        
    p2 = str(input("Escribe el número 21 en alemán: "))
    if p2 == "einundzwanzig":
        count += 1
    else:
        count += 0
    
    p3 = str(input("Escribe el número 11 en alemán: "))
    if p3 == "elf":
        count += 1
    else:
        count += 0
    
    p4 = str(input("Escribe el número 53 en alemán: "))
    if p4 == "dreiundfünfzig":
        count += 1
    else:
        count += 0
    
    p5 = str(input("Escribe el número 100 en alemán: "))
    if p5 == "hundert" or p5 == "einhundert":
        count += 1
    else:
        count += 0
    
    puntaje_total = calculadora(count)
    print("Puntaje total:", puntaje_total)
    
    menu_opciones = str(input("Si deseas volver a la sección anterior teclea ´si´.Para el menú principal teclea 'm´: "))
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            numeros_seccion = numeros()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("Si deseas volver a la sección anterior teclea ´si´.Para el menú principal teclea 'm´: "))
        break

"""Esta función se encarga de mostrar la información sobre los numeros en alemán.
Tambén dirige con un condicional al usuario hacia la practica o devuelta la menú."""
def numeros():
    print("\nAprendamos a contar en Alemán del 1 - 100. \nPrimero memoriza los numeros del 1 - 9.")
    print("neins - 1, zwei - 2, drei - 3, vier - 4, fünf - 5, sechs - 6, sieben - 7, acht - 8, neun - 9")
    print("\nAhora contemos de 10 en 10.")
    print("zehn - 10, zwanzig - 20, dreißig - 30, vierzig - 40, fünfzig - 50, sechzig - 60, siebzig - 70, \nachtzig - 80, neunzig - 90, einhundert/hundert - 100")
    print("\nPor último aprenderemos a contar los numeros de dos digitos, para cada decena se sigue la misma regla.")
    print("Sin embargo, es importante recordar que los siguientes numeros no siguen la regla: elf - 11, zwölf - 12")
    print("\nContemos del 21 - 29, dónde primero mencionaremos la unidad y después la decena.")
    print("einundzwanzig - 21, zweiundzwanzig - 22, dreiundzwanzig - 23, vierundzwanzig - 24, fünfundzwanzig - 25 \nsechsundzwanzig - 26, siebenundzwanzig - 27, achtundzwanzig - 28, neunundzwanzig - 29")
    
    menu_opciones = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea 'm´: "))
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            numeros_actividad = quiznum()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea 'm´: "))
        break
            
"""Esta función se encarga de calcular el promedio en las actividades de practica
y quizes utilizando operadores."""
def calculadora(p):
    promedio = int((p*100)/5)
    return(promedio)

#Esta función se encarga de imprimir el menu principal. 
def menu():
    print("\n Selecciona la opcion para aprender el día de hoy escribiendo el numero.\n")
    print("1. Los números")
    print("2. Artículos: der die das")
    print("0. Salir del programa")

"""Esta función mantiene el programa corriendo con un ciclo while hasta que el usuario decida
salir del programa. También se encarga de dirigar al usuario a la sección que quiere estudiar. """
def main():
    while True:
        inicio = menu()
        opcion = str(input("Ingresa la opción: "))
        if opcion == "1":
            seccion_numeros = numeros()
        elif opcion == "2":
            seccion_articulos = articulos()
        elif opcion == "0":
            print("Gracias, vuelve pronto.")
            break
        else:
            print("Opción invalida.")
        
main()
