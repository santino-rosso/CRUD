import unittest
from unittest.mock import patch
from persona import Persona
from personaService import PersonaService
import os


class TestPersona(unittest.TestCase):
    
    def crearArchivo(self):
        self.archivo = open("/home/santino/Escritorio/crud/persona","w") 
        self.archivo.close()

    def test_Crear_Archivo(self):       
        self.crearArchivo()
        self.assertTrue(os.path.exists("/home/santino/Escritorio/crud/persona"))

    @patch('builtins.input', return_value='si')
    def test_archivo_vacio(self,value):
        self.crearArchivo()
        personaService = PersonaService()
        personaService.findAll()
        with open("/home/santino/Escritorio/crud/persona","r") as archivo:
            self.assertFalse(None in archivo.read())

    @patch('builtins.input', return_value='si')
    def test_Eliminar_Persona(self,value):
        self.crearArchivo()
        persona = Persona(1,"Perez","Juan")
        personaService = PersonaService()
        personaService.add(persona.documento,persona.apellido,persona.nombre)
        personaService.delete(persona.documento)
        with open("/home/santino/Escritorio/crud/persona","r") as archivo:
            self.assertFalse("Documento: 1 - Apellido: Perez, Nombre: Juan" in archivo.read())

    

    def test_Verificar_Tamano_Archivo(self):
        self.crearArchivo()
        persona = Persona(1,"Perez","Juan")
        personaService = PersonaService()
        personaService.add(persona.documento,persona.apellido,persona.nombre)
        self.assertTrue(os.path.getsize("/home/santino/Escritorio/crud/persona") > 0)

    def test_Verificar_Contenido_Archivo(self):
        self.crearArchivo()
        persona = Persona(1,"Perez","Juan")
        personaService = PersonaService()
        personaService.add(persona.documento,persona.apellido,persona.nombre)
        with open("/home/santino/Escritorio/crud/persona","r") as archivo:
            self.assertTrue("Documento: 1 - Apellido: Perez, Nombre: Juan" in archivo.read())

    @patch('builtins.input', return_value='si')
    def test_Verificar_Contenido_Archivo_Modificar(self,value):
        self.crearArchivo()
        persona = Persona(1,"Perez","Juan")
        personaService = PersonaService()
        personaService.add(persona.documento,persona.apellido,persona.nombre)
        personaService.update(1,2,"Gomez","Jose")
        with open("/home/santino/Escritorio/crud/persona","r") as archivo:
            self.assertTrue("Documento: 2 - Apellido: Gomez, Nombre: Jose" in archivo.read())

    
    @patch('builtins.input', return_value='si')
    def test_Verificar_Contenido_Archivo_Buscar(self,value):
        self.crearArchivo()
        persona = Persona(1,"Perez","Juan")
        personaService = PersonaService()
        personaService.add(persona.documento,persona.apellido,persona.nombre)
        personaService.findByDocumento(1)
        with open("/home/santino/Escritorio/crud/persona","r") as archivo:
            self.assertTrue("Documento: 1 - Apellido: Perez, Nombre: Juan" in archivo.read())
        
    @patch('builtins.input', return_value='si')
    def test_Verificar_Contenido_Archivo_Listar(self,value):
        self.crearArchivo()
        persona = Persona(1,"Perez","Juan")
        personaService = PersonaService()
        personaService.add(persona.documento,persona.apellido,persona.nombre)
        personaService.findAll()
        with open("/home/santino/Escritorio/crud/persona","r") as archivo:
            self.assertTrue("Documento: 1 - Apellido: Perez, Nombre: Juan" in archivo.read())

    @patch('builtins.input', return_value='si')
    def test_archivo_vacio(self,value):
        self.crearArchivo()
        personaService = PersonaService()
        personaService.findAll()
        with open("/home/santino/Escritorio/crud/persona","r") as archivo:
            self.assertFalse("Documento: 1 - Apellido: Perez, Nombre: Juan" in archivo.read())

    

if __name__ == "__main__":
    unittest.main()