import os

class PersonaService:

  def add(self, documento, apellido, nombre):
    with open("/home/santino/Escritorio/crud/persona","a") as archivo:
      archivo.write(f'Documento: {documento} - Apellido: {apellido}, Nombre: {nombre}' + os.linesep)
    print("Se agrego la persona")

  def delete(self, documento):
    x=""
    with open("/home/santino/Escritorio/crud/persona","r") as archivo:
      for linea in archivo:
        if linea.startswith(f'Documento: {documento}'):
          print(linea)
          print("\n")
          print("Esta seguro que desea eliminar esta persona?")
          print("\n")
          opcion = input("Ingrese una opcion(si/no): ")
          print("\n")
          if opcion == "si":
            linea = ""
            x = x + linea
            print("Se elimino la persona")
          else:
            print("No se elimino la persona")
        else:
          x = x + linea
      with open("/home/santino/Escritorio/crud/persona","w") as archivo:
        archivo.write(x)

  def update(self, documento1,documento2, apellido, nombre):
    x=""
    with open("/home/santino/Escritorio/crud/persona","r") as archivo:
      for linea in archivo:
        if linea.startswith(f'Documento: {documento1}'):
          print(linea)
          print("\n")
          print("Esta seguro que desea modificar esta persona?")
          print("\n")
          opcion = input("Ingrese una opcion(si/no): ")
          print("\n")
          if opcion == "si":
            linea = (f'Documento: {documento2} - Apellido: {apellido}, Nombre: {nombre}' + os.linesep)
            x = x + linea
            print("Nuevos datos de la persona:",linea)
          else:
            print("No se modifico la persona")
        else:
          x = x + linea
      with open("/home/santino/Escritorio/crud/persona","w") as archivo:
        archivo.write(x)

  def findByDocumento(self, documento):
    with open("/home/santino/Escritorio/crud/persona","r") as archivo:
      for linea in archivo:
        if linea.startswith(f'Documento: {documento}'):
          print("Persona encontrada: ",linea)
  
  def findAll(self):
    with open("/home/santino/Escritorio/crud/persona","r") as archivo:
      print("---Registro de personas---")
      print("\n")
      for linea in archivo:
        print(linea)

  


  

