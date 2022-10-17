class Vehiculos():
    def __init__(self, color, ruedas, puertas):
        self.color=color
        self.ruedas=ruedas
        self.puertas=puertas

class Coche(Vehiculos):    
    def __init__(self, velocidad, cilindrada):
        self.velocidad=velocidad
        self.cilindrada=cilindrada

c1=Coche(200,1500)
print("El coche creado tiene una velocidad de" , c1.velocidad,"Km/h y una cilindrada de", c1.cilindrada,"cc")

