class cursotemavideo:

    def __init__(self, idCursoTV, idCT, idV):
        self.idCursoTV = idCursoTV
        self.idCT = idCT
        self.idV = idV

    @property
    def idCursoTV(self):
        return self.__idCursoTV
    
    @idCursoTV.setter
    def idCursoTV(self, valor):
        self.__idCursoTV = valor

    @property
    def idCT(self):
        return self.__idCT
    
    @idCT.setter
    def idCT(self, valor):
        self.__idCT = valor

    @property
    def idV(self):
        return self.__idV
    
    @idV.setter
    def idV(self, valor):
        self.__idV = valor

    def agregar(self):
        archivo = open("./archivos/Curso_Tema_Video.txt", 'a')
        archivo.write(f"{self.idCursoTV} / {self.idCT} / {self.idV}  \n")
        archivo.close()

    def borrar(self):
        archivo = open("./archivos/Curso_Tema_Video.txt", 'r')
        lineas = archivo.readlines()
        archivo.close()
        archivo = open("./archivos/Curso_Tema_Video.txt", 'w')
        for linea in lineas:
            if linea != (f"{self.idCursoTV} / {self.idCT} / {self.idV}  \n"):
                archivo.write(linea)
        archivo.close()
    
    def consultar(self):
        archivo = open("./archivos/Curso_Tema_Video.txt", 'r')
        print("\n")
        print(archivo.read())
        archivo.close()