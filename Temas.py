class Tema:
    def __init__(self,idTema,nombre):
        self.idTema = idTema
        self.nombre = nombre

    @property 
    def idTema(self):
        return self.__idTema

    @idTema.setter
    def idTema(self, valor):
        self.__idTema = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    def agregar(self):
        archivo=open("./archivos/Temas.txt", 'a')
        archivo.write(f"{self.idTema} / {self.nombre} \n")
        archivo.close()

    def borrar(self):
        archivo=open("./archivos/Temas.txt", "r")
        lineas=archivo.readlines()
        archivo.close()
        archivo=open("./archivos/Temas.txt", "w")
        for linea in lineas:
            if linea != (f"{self.idTema} / {self.nombre} \n"):
                archivo.write(linea)
        archivo.close()

    def consultar(self):
        archivo=open("./archivos/Temas.txt", 'r')
        print("\n")
        print (archivo.read())
        archivo.close()
        
        
