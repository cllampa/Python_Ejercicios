ingresarPaises= (input("Ingrese el nombre de Spaíses separados sólo por comas: "))

lstPaises=ingresarPaises.split(",")

lstSinDuplicados=set(lstPaises)

lstPaisesOrdenados=sorted(lstSinDuplicados)

def main():
    print(lstPaisesOrdenados)

if __name__=='__main__':
    main()