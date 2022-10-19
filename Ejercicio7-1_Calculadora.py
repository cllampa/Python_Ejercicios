import Operadores.suma as opsuma
import Operadores.resta as opresta
import Operadores.multiplicacion as opmultiplicacion
import Operadores.division as opdivision

a=int(input("Ingrese el primer numero: "))   
b=int(input("Ingrese el segundo numero: "))   

def main():
    print("La suma es igual a ",int(opsuma.suma(a,b)))
    print("La resta es igual a ",int(opresta.resta(a,b)))
    print("La multiplicación es igual a ",int(opmultiplicacion.multiplicacion(a,b)))
    print("La division es igual a ",int(opdivision.division(a,b)))

if __name__== '__main__':
    main()