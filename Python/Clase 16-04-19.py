def sumar (x,y,c):
    sum = x+y+c
    c = 20
    return sum 

def par(a):
    if a % 2 == 0:
        par = True
    else:
        par = False
    return par


a = 7 #int (input("Ingrese entero A\n"))
b = 8 #int (input("Ingrese entero B\n"))
c = 2
print (sumar(a,b,c))
print (par(a))
