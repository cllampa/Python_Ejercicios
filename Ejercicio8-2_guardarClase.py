import pickle


  
class Vehiculos():
    def __init__(self, color, ruedas, puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

    def getColor(self):
        return self.color

v1=Vehiculos("rojo",4,5)

with open("txtClase.bin","wb") as file:
    pickle.dump(v1,file)

with open("txtClase.bin", "rb") as file:
    vehiculo=pickle.load(file)

def main():
    print(vehiculo.getColor())

if __name__=='__main__':
    main()