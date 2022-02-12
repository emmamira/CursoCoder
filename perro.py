class Perro:
    #Atributos de calse
    especie="Mamífero"

    #Constructor de clase
    def __init__(self, nombre, raza):

        #Atributos de instancia
        self.nombre = nombre
        self.raza = raza
    
    def ladra(self):
        print("Guau")

    def camina(self,pasos):
        print(f"Caminando {pasos} pasos")

perro1 = Perro("Samy","Caniche")

print("Su nombre es:", perro1.nombre)
print("Su raza es:", perro1.raza)
print("Es un:", perro1.especie)
perro1.ladra()
perro1.camina(5)