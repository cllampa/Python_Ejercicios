from functools import reduce

listado=[0,1,2,3,4,5,6,7,8,9]

def Impares(x):
    if x%2 != 0:
        return True
    return False

def Suma(a,b):
    return a + b

filterImpares=filter(Impares,listado)

lstImpares=list(filterImpares)

reduceSuma=reduce(Suma,lstImpares)

def main():
    print(lstImpares)
    print(reduceSuma)

if __name__=='__main__':
    main()