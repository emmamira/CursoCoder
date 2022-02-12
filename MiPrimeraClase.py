class persona:
    #Atributo de clase
    especie = "humano"
    nivel_desarrollo = "máximo"

    #Constructor de clase
    def __init__ (self,nombre,edad,profesión):
        print(f"Soy {nombre}, tengo {edad} años y trabajo de {profesión}")
        #Atributos de instancia
        self.nombre=nombre
        self.edad=edad
        self.profesión=profesión

    #Métodos
    def saludar(self):
        print("Hola")
        
    def caminar(self,pasos):
        print(f"esta personas caminó {pasos} pasos")

persona1 = persona("Juan",20,"contador")


persona1.saludar()
persona1.caminar(20)




