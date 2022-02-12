class Persona:
    #Atributos de clase
    especie= "Ser humano"
    estado= "vivo"
    
    #Constructor de clase
    def __init__ (self,nombre,edad,profesion):
        print(f"Soy {nombre}, tengo {edad} años y trabajo de {profesion}")
        #Atributos de instancia
        self.nombre=nombre
        self.edad=edad
        self.profesion=profesion
        
    def saludar(self):
        print("Hola, buenos días")
    
    def trabajar (self,horas):
        print(f"Trabajo {horas} horas por día")
        
persona1= Persona("Mariana",25,"Analista")
persona1.saludar()
persona1.trabajar(8)
