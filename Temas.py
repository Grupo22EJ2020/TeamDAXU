class Tema:
    def __init__(self,idTema,nombre):
        self.idTema = idTema
        self.nombre = nombre

@property 
def idTema(self):
    return self.idTema

@idTema.setter
def idTema(self, valor):
    self.__idTema = valor

@property
def nombre(self):
    return self.nombre

@nombre.setter
    archivo.close()

def agregar(self):
    archivo=open("./archivos/Tema.txt", 'a')
    idTema=(input("Ingresa el id del tema: n/")) 
    nombre=(input("Ingresa el nombre del tema: n/"))
    archivo=write(f"{self.idTema} / {self.nombre} \n")
    archivo.close()




