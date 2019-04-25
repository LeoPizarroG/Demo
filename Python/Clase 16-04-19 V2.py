def menu ():
    print ("Para Sumar marca 1\n")
    print ("Para Multiplicar marca 2\n")
    print ("Para Restar marca 3\n")
    opcion = int (input("Elije una opcion\n"))
    return opcion

def restar (a,b):
    rest = a-b
    return rest
def sumar (a,b):
    sumar = a+b
    return sumar

def multi (a,b):
    mul = a*b
    return mul

restar(a,b)=restar(a,b)
sumar(a,b)=sumar(a,b)
multi(a,b)=multi(a,b)

a = 7
b = 8

if menu() == 1:
    print (sumar(a,b),"\n")

elif menu() == 2:
    print (multi(a,b),"\n")
    
elif menu() == 3:
    print (restar(a,b),"\n")