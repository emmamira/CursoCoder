class Atleta:
    def __init__ (self,nombre,apellido,altura,peso,__teléfono,IMC) -> None:
        
        #Atributos de instancia
        self.nombre=nombre
        self.apellido=apellido
        self.altura=altura
        self.peso=peso
        self.__teléfono=teléfono
        self.IMC=(peso/(altura*altura)

    def get_IMC(self):
        return self.IMC

    def __setitem__(self, pos, value):
        self.teléfono[pos] = value
        
