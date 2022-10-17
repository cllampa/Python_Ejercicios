class Alumno:
    def __init__(self, name, nota):
        self.name = name
        self.nota = nota
    
    def mostrarInformacion(self):
        print("Nombre:", self.name)
        print("Nota:", self.nota)


    def obtenerCondicion(self):
        if self.nota <= 4:
            condicion="desaprobado"
        else:
            condicion="aprobado"
        print("Su condicion es", condicion)

a1=Alumno("Cristian", 10)
a1.mostrarInformacion()
a1.obtenerCondicion()