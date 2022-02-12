#definimos las clases padre
class Mamífero:
    def __init__ (self, cant_mamas, esp_de_vida) -> None:
        self.cant_mamas = cant_mamas
        self.esp_de_vida = esp_de_vida
    
    def mamar(self):
        pass
    
    def nacer(self):
        pass

class AnimalMarino:
    def __init__ (self, tiene_branqueas, especie) -> None:
        self.tiene_branqueas = tiene_branqueas
        self.especie = especie
    
    def nadar(self):
        pass

#creamos la clase hija
class Cetáceo(Mamífero, AnimalMarino)
    def __init__ (self, cant_mamas, esp_de_vida, tiene_branqueas, especie, notas, vive_en, peso) -> None:
        Mamífero.super().__init__(cant_mamas, esp_de_vida)
        AnimalMarino.super().__init__(tiene_branqueas, especie)
        self.notas = notas
        self.vive_en = vive_en
        self.peso = peso
    
    def nacer(self):
        pass
    
    def nadar(self):
        pass

ballena_azul = Cetáceo ("Animla más grande de todos","Mar", 110000)

