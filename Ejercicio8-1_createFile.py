from genericpath import exists

def main():
    
    if not exists ("datos.txt"):
        with open("datos.txt", "w") as file:
            file.write("")
       
    else:
        txtIngresado=(input("Ingrese el texto que desea guardar: "))
        
        while len(txtIngresado)>0:
            with open("datos.txt", "a") as file:
                file.write(txtIngresado)
                file.write("\n")
                txtIngresado=(input("Ingrese el texto que desea guardar: "))
        print("No ha ingresado un texto. ")

if __name__=='__main__':
    main()