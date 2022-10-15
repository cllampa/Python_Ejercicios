año=int(input("Ingrese un año: "))

def añoBisiesto(año):
    if año%100==0 and año%400==0:
        return True
    elif año%4==0 and año%100!=0:
        return True
    else:
        return False

if añoBisiesto(año):
    print("El año" ,año, "es bisiesto")
else:
    print("El año",año, "no es bisiesto")
       