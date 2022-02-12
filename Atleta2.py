class Atleta:
    def __init__ (self, Nombre, Apellido):
        print(f"Nombre: {Nombre}\nApellido: {Apellido}\nIMC:{Atleta1.calculo_IMC(87,1.80)}\nTeléfono: {Atleta1.getNumeroTelefonico()}")
        self.Nombre = Nombre
        self.Apellido = Apellido
        self.__Telefono = "0303456"

    def calculo_IMC (self, Peso, Altura):
        return Peso/Altura/Altura
    
    def getNumeroTelefonico(self):
        return self.__Telefono


Atleta1= Atleta("Usain", "Bolt")

