"""
Programa para aprender alemán
El programa está formado por 5 secciones para aprender el idioma.
Cada una de ellas cuenta con una explicación del tema y ejercicios
de práctica dónde se evalúan las respuestas del usuario para mostrar
el puntaje alcanzado así como los conocimientos obtenidos. 
"""

"""En esta función el usuario practica el tema de frases. Primero se despliega un texto incorrecto utilizando
strings para que despues el usuario lo separe y lo reacomode a traves de las preguntas. Si el texto es correcto
este se imprimira de nuevo con su puntaje, de lo contrario el usuario debera seguir estudiando para volver a intentarlo. 
"""
def practica_frases():
    print("Separa y acomoda el siguiente texto en orden.")
    count = 0
    
    f1 = "Guten Morgen, Herr Müller!"
    f2 = "Wie geht es Ihnen?"
    f3 = "Gut danke und Sie?"
    f4 = "Mir geht es auch gut."
    f5 = "Es freut mich, dich kennen zu lernen."
    texto_incorrecto = (f5 + f2 + f3 + f1+ f4)

    for i in range(len(texto_incorrecto)):
        print("%c" % texto_incorrecto[i], end="")

    print("\n")
    p1 = str(input("Ingrese frase 1: "))
    if p1 == "Guten Morgen, Herr Müller!":
        count += 1
    else:
        count += 0
    
    p2 = str(input("Ingrese frase 2: "))
    if p2 == "Wie geht es Ihnen?":
        count += 1
    else:
        count += 0
   
    p3 = str(input("Ingrese frase 3: "))
    if p3 == "Gut danke und Sie?":
        count += 1
    else:
        count += 0
    
    p4 = str(input("Ingrese frase 4: "))
    if p4 == "Mir geht es auch gut.":
        count += 1
    else:
        count += 0

    p5 = str(input("Ingrese frase 5: "))
    if p5 == "Es freut mich, dich kennen zu lernen.":
        count += 1
    else:
        count += 0
        
    if count == 5:
        print("\nTexto correcto:\nGuten Morgen, Herr Müller!\nWie geht es Ihnen?\nGut danke und Sie?")
        print("Mir geht es auch gut.Es freut mich, dich kennen zu lernen.")
    else:
        print("El texto no es correcto. Sigue estudiando e inténtalo de nuevo")
    
    puntaje_total = calculadora(count)
    print("Puntaje total:", puntaje_total)
    
    m_p = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower()
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            frases_seccion = frases()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
        break

"""Esta función se encarga de mostrar la información sobre frases útiles en alemán.
Tambén dirige con un condicional al usuario hacia la practica o devuelta la menú."""
def frases():
    file = open("frases.txt","r")
    contenido = file.read()
    print(contenido)
    file.close()
    
    m_p = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower()
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            presentarse_actividad = practica_frases()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
        break

"""En esta función se realizan ejercicios de opcion multiple con el uso de condicionales
para practicar el tema de cómo presentarse en alemán. Se muestra al final el puntaje obtenido."""
def practica_presentarse():
    count = 0
    print("\nEscribe la letra con la respuesta correcta en el ejercicio de opción multiple")
    print("\nMein ____ ist ...")
    print("a.Name\nb.Nam\nc.name")
    p_1 = str(input())
    p1 = p_1.lower()
    if p1 == "a":
        count += 1
    else:
        count += 0
    
    print("\nYo soy...")
    print("a.Ich bist\nb.Ich bin\nc.Ich sein")
    p_2 = str(input())
    p2 = p_2.lower()
    if p2 == "b":
        count += 1
    else:
        count += 0
    
    print("Ich heiße ...")
    print("a.Yo soy...\nb.Yo me llamo...\nc.Mi nombre es...")
    p_3 = str(input())
    p3 = p_3.lower()
    if p3 == "b":
        count += 1
    else:
        count += 0
    
    print("\n¿Cómo se llama usted?")
    print("a.Wie heißen sie?\nb.Wie heißen Ihr?\nc.Wie heißen Sie?")
    p_4 = str(input())
    p4 = p_4.lower()
    if p4 == "c":
        count += 1
    else:
        count += 0
    
    print("\n¿Cómo te llamas?")
    print("a.Wie heißt du?\nb.Wie heißt dir?\nc.Wie heißt ihr?")
    p_5 = str(input())
    p5 = p_5.lower()
    if p5 == "a":
        count += 1
    else:
        count += 0
    
    puntaje_total = calculadora(count)
    print("Puntaje total:", puntaje_total)
    
    m_p = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower()
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            presentarse_seccion = presentarse()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
        break

"""Esta función se encarga de mostrar la información sobre cómo presentarse en alemán.
Tambén dirige con un condicional al usuario hacia la practica o devuelta la menú."""
def presentarse():
    file = open("presentarse.txt","r")
    contenido = file.read()
    print(contenido)
    file.close()
    
    m_p = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower()
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            presentarse_actividad = practica_presentarse()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
        break

""" Esta funcion tiene una serie de ejercicios para practicar las conjugaciones de los verbos.
Contiene dos matrices. En la primera matriz dentro de la primera lista se encuentran los
pronombres, mientras que la segunda lista esta vacia y será llenada por el usuario mediante
un ciclo for con los verbos. La segunda matriz tiene las respuestas correctas en caso de
que el usuario tenga las respuestas incorrectas. Se muestra el puntaje al final."""
def practica_verbos():
    count = 0
    
    print("Conjuga el verbo 'sein'.")
    matriz_s = [["ich","du","er/sie/es","wir","ihr", "Sie/sie"],[]]
    matriz_sr =[["ich","du","er/sie/es","wir","ihr", "Sie/sie"],["bin","bist","ist","sind","seid", "sind"]]
    for i in range(len(matriz_s[0])):
        print(matriz_s[0][i])
        palabra = str(input())
        matriz_s[1].insert(i,palabra)
    print(matriz_s[0],"\n",matriz_s[1])

    if matriz_s == matriz_sr:
        count += 1
    else:
        print("La respuesta correcta es: \n", matriz_sr[0],"\n",matriz_sr[1])

    print("Conjuga el verbo 'haben'.")
    matriz_h = [["ich","du","er/sie/es","wir","ihr", "Sie/sie"],[]]
    matriz_hr =[["ich","du","er/sie/es","wir","ihr", "Sie/sie"],["habe","hast","hat","haben","habt", "haben"]]
    for i in range(len(matriz_h[0])):
        print(matriz_h[0][i])
        palabra = str(input())
        matriz_h[1].insert(i,palabra)
    print(matriz_h[0],"\n",matriz_h[1])

    if matriz_h == matriz_hr:
        count += 1
    else:
        print("La respuesta correcta es: \n", matriz_hr[0],"\n",matriz_hr[1])

    print("Conjuga el verbo 'lernen' que significa aprender.")
    matriz_l = [["ich","du","er/sie/es","wir","ihr", "Sie/sie"],[]]
    matriz_lr =[["ich","du","er/sie/es","wir","ihr", "Sie/sie"],["lerne","lernst","lernt","lernen","lernt", "lernen"]]
    for i in range(len(matriz_l[0])):
        print(matriz_l[0][i])
        palabra = str(input())
        matriz_l[1].insert(i,palabra)
    print(matriz_l[0],"\n",matriz_l[1])

    if matriz_l == matriz_lr:
        count += 1
    else:
        print("La respuesta correcta es: \n", matriz_lr[0],"\n",matriz_lr[1])
        
    print("Conjuga el verbo 'machen' que significa hacer.")
    matriz_m = [["ich","du","er/sie/es","wir","ihr", "Sie/sie"],[]]
    matriz_mr =[["ich","du","er/sie/es","wir","ihr", "Sie/sie"],["mache","machst","macht","machen","macht", "machen"]]
    for i in range(len(matriz_m[0])):
        print(matriz_m[0][i])
        palabra = str(input())
        matriz_m[1].insert(i,palabra)
    print(matriz_m[0],"\n",matriz_m[1])

    if matriz_m == matriz_mr:
        count += 1
    else:
        print("La respuesta correcta es: \n", matriz_mr[0],"\n",matriz_mr[1])

    print("Conjuga el verbo 'gehen' que significa ir.")
    matriz_g = [["ich","du","er/sie/es","wir","ihr", "Sie/sie"],[]]
    matriz_gr =[["ich","du","er/sie/es","wir","ihr", "Sie/sie"],["gehe","gehst","geht","gehen","geht", "gehen"]]
    for i in range(len(matriz_g[0])):
        print(matriz_g[0][i])
        palabra = str(input())
        matriz_g[1].insert(i,palabra)
    print(matriz_g[0],"\n",matriz_g[1])

    if matriz_g == matriz_gr:
        count += 1
    else:
        print("La respuesta correcta es: \n", matriz_gr[0],"\n",matriz_gr[1])
    
    puntaje_total = calculadora(count)
    print("Puntaje total:",puntaje_total)
    
    m_p = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower()
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            verbos_seccion = verbos()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
        break
    
""" Esta función se encarga de mostrar la información sobre los verbos en alemán.
Tambén dirige con un condicional al usuario hacia la practica o devuelta la menú."""
def verbos():
    file = open("verbos.txt","r")
    contenido = file.read()
    print(contenido)
    file.close()
    
    m_p = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower()
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            verbos_actividad = practica_verbos()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
        break

"""Esta función contiene una actividad de practica con ejercicios para repasar los articulos.
Utiliza condicionales así como operadores para sumar los puntos obtenidos en el quiz y después
enviarlos a la función del promedio para que el usuario vea su puntaje total."""
def practica_articulos():
    count = 0
    print("Escribe el articulo correspondiente para cada palabra.\nTendras tres oportunidades para sacar bien la respuesta.\nObtendras el punto solo si la respuesta es correcta en el primer intento.")
    
    for cont1 in range (0,3):
        p_1 = str(input("Haus, der die das: "))
        p1 = p_1.lower()
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
        p_2 = str(input("Computer, der die das: "))
        p2 = p_2.lower()
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
        p_3 = str(input("Mann, der die das: "))
        p3 = p_3.lower()
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
        p_4 = str(input("Sonne, der die das: "))
        p4 = p_4.lower()
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
        p_5 = str(input("Mädchen, der die das: "))
        p5 = p_5.lower()
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
    
    m_p = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower()
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            articulos_seccion = articulos()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
        break
    
"""Esta función se encarga de mostrar la información sobre los articulos en alemán.
Tambén dirige con un condicional al usuario hacia la practica o devuelta la menú."""
def articulos():
    file = open("articulos.txt","r")
    contenido = file.read()
    print(contenido)
    file.close()
    
    m_p = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower()
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            articulos_actividad = practica_articulos()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
        break
    
"""Esta función contiene un quiz con ejercicios para practicar los numeros.
Utiliza condicionales y operadores para sumar los puntos obtenidos en el quiz y después
enviarlos a la función del promedio para que el usuario vea su puntaje total."""
def quiznum():
    count = 0
    
    p_1 = str(input("Escribe el número 8 en alemán: "))
    p1 = p_1.lower()
    if p1 == "acht":
        count += 1
    else:
        count += 0
        
    p_2 = str(input("Escribe el número 21 en alemán: "))
    p2 = p_2.lower()
    if p2 == "einundzwanzig":
        count += 1
    else:
        count += 0
    
    p_3 = str(input("Escribe el número 11 en alemán: "))
    p3 = p_3.lower()
    if p3 == "elf":
        count += 1
    else:
        count += 0
    
    p_4 = str(input("Escribe el número 53 en alemán: "))
    p4 = p_4.lower()
    if p4 == "dreiundfünfzig":
        count += 1
    else:
        count += 0
    
    p_5 = str(input("Escribe el número 100 en alemán: "))
    p5 = p_5.lower()
    if p5 == "hundert" or p5 == "einhundert":
        count += 1
    else:
        count += 0
    
    puntaje_total = calculadora(count)
    print("Puntaje total:", puntaje_total)
    
    m_p = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower() 
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            numeros_seccion = numeros()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas volver a la sección anterior teclea´si´.Para el menú principal teclea ´m´: "))
        break

"""Esta función se encarga de mostrar la información sobre los numeros en alemán.
Tambén dirige con un condicional al usuario hacia la practica o devuelta la menú."""
def numeros():
    #No se utilizó un archivo para la información debido a los caracteres especiales.
    print("\nAprendamos a contar en Alemán del 1 - 100. \nPrimero memoriza los numeros del 1 - 9.")
    print("neins - 1, zwei - 2, drei - 3, vier - 4, fünf - 5, sechs - 6, sieben - 7, acht - 8, neun - 9")
    print("\nAhora contemos de 10 en 10.")
    print("zehn - 10, zwanzig - 20, dreißig - 30, vierzig - 40, fünfzig - 50, sechzig - 60, siebzig - 70, \nachtzig - 80, neunzig - 90, einhundert/hundert - 100")
    print("\nPor último aprenderemos a contar los numeros de dos digitos, para cada decena se sigue la misma regla.")
    print("Sin embargo, es importante recordar que los siguientes numeros no siguen la regla: elf - 11, zwölf - 12")
    print("\nContemos del 21 - 29, dónde primero mencionaremos la unidad y después la decena.")
    print("einundzwanzig - 21, zweiundzwanzig - 22, dreiundzwanzig - 23, vierundzwanzig - 24, fünfundzwanzig - 25 \nsechsundzwanzig - 26, siebenundzwanzig - 27, achtundzwanzig - 28, neunundzwanzig - 29")
    
    m_p = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
    menu_opciones = m_p.lower() 
    while menu_opciones != "si" or menu_opciones != "m":
        if menu_opciones == "si":
            numeros_actividad = quiznum()
        elif menu_opciones == "m":
            menu_principal = main()
        else:
            print("Ingresa opción valida")
            menu_opciones = str(input("\nSi deseas ir a la practica teclea ´si´.Para el menú principal teclea ´m´: "))
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
    print("3. Verbos")
    print("4. Cómo presentarse")
    print("5. Frases útiles")
    print("0. Salir del programa.")

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
        elif opcion == "3":
            seccion_verbos = verbos()
        elif opcion == "4":
            seccion_presentarse = presentarse()
        elif opcion == "5":
            seccion_frases = frases()
        elif opcion == "0":
            print("Gracias, vuelve pronto.")
            break
        else:
            print("Opción invalida. Vuelve pronto.")
        break

main()