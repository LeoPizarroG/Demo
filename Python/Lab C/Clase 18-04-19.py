
def restar ():
    casos = int(input ("Cuantas operaciones deseas hacer?\n"))
    resta = 0
    contador = 1 
    primerresta = True
    while contador <= casos:
        num1 = int(input("Ingresa entero \n")) 
        if primerresta == True:
            resta = num1
            primerresta = False
            contador += 1
        else: 
            resta = resta - num1
            contador += 1
    return resta
def sumar ():
    casos = int(input ("Cuantas operaciones deseas hacer?\n"))
    sumar = 0
    contador = 1 
    while contador <= casos:
        num1 = int(input("Ingresa entero \n")) 
        sumar = sumar + num1
        contador += 1
    return sumar

def multi ():
    parar = False
    multi = 1
    while parar == False:
        num1 = str(input("Ingresa entero \n"))
        if num1 == "Parar":
            parar = True
        else: 
            num2 = int(num1)
            multi = multi * num2
            print ("Resultado es: ",multi)
    return multi

def divisi ():
    parar = False
    divi = 0
    diviprimer = True
    while parar == False:
        num1 = str(input("Ingresa entero \n"))
        if num1 == "Parar":
            parar = True
        elif diviprimer == True:
            num2 = int(num1)
            divi = num2
            diviprimer = False
        else: 
            num2 = int(num1)
            divi = divi / num2
            print ("Resultado es: ",divi)
    return divi
def menu ():
    print ("Calculadora:")

    print ("Para Sumar apreta 1:\n")
    print ("Para Restar apreta 2:\n")
    print ("Para Multiplicar apreta 3:\n")
    print ("Para Dividir apreta 4:\n")
    print ("Para Salir apreta 5:\n") 
    opcion = int (input("Ingrese una Opcion\n"))
    return opcion

loop = True

while loop == True:
    if menu() == 1:
        print ("El resultado es:",sumar())
        menu()

    elif menu() == 2:
        print ("El resultado es:",restar())
        menu()

    elif menu() == 3:
        print ("El resultado es:",multi())
        menu()

    elif menu() == 4:
        print ("El resultado es:",divisi())
        menu()

    elif menu() == 5:
        loop = False
        print ("Adios\n")
    
    else: 
        print ("Ingresa opcion valida:\n")
        menu()