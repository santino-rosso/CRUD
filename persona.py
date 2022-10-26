from personaService import PersonaService

class Persona:
    def __init__(self, documento=0, apellido="", nombre=""):
        self.documento = documento
        self.apellido = apellido
        self.nombre = nombre
        self.persona_Service = PersonaService()

    def input(self):
        while True:
            print("Eliga una opcion: ")
            print("\n")
            print("1. Agregar persona")
            print("2. Eliminar persona")
            print("3. Modificar persona")
            print("4. Buscar persona")
            print("5. Mostrar a todos")
            print("6. Salir")
            print("\n")
            opcion = int(input("Ingrese una opcion: "))
            print("\n")
            if opcion == 1:
                self.documento = int(input('Ingrese documento: '))
                self.apellido = input('Ingrese apellido: ')
                self.nombre = input('Ingrese nombre: ')
                print("\n")
                self.persona_Service.add(self.documento, self.apellido, self.nombre)
                print("\n")
            elif opcion == 2:
                self.documento = int(input('Ingrese documento: '))
                print("\n")
                self.persona_Service.delete(self.documento)
                print("\n")
            elif opcion == 3:
                self.documento1 = int(input('Ingrese documento de la persona que quiere modificar: '))
                print("\n")
                self.documento2 = int(input('Ingrese nuevo documento: '))
                self.apellido = input('Ingrese nuevo apellido: ')
                self.nombre = input('Ingrese nuevo nombre: ')
                print("\n")
                self.persona_Service.update(self.documento1,self.documento2, self.apellido, self.nombre)
                print("\n")
            elif opcion == 4:
                self.documento = int(input('Ingrese documento de la persona que quiere buscar: '))
                print("\n")
                self.persona_Service.findByDocumento(self.documento)
                print("\n")
            elif opcion == 5:
                self.persona_Service.findAll()
                print("\n")
            elif opcion == 6:
                print("Gracias por usar el programa")
                break



