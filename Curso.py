class curso:
    
    def __init__(self, idCurso, descripcion, idEmpleado):
        self.idCurso = idCurso
        self.descripcion = descripcion
        self.idEmpleado = idEmpleado

    @property
    def idCurso(self):
        return self.__idCurso

    @idCurso.setter
    def idCurso(self, valor):
        self.__idCurso = valor

    @property
    def descripcion(self):
        return self.__descripcion

    @descripcion.setter
    def descripcion(self, valor):
        self.__descripcion = valor

    @property
    def idEmpleado(self):
        return self.__idEmpleado

    @idEmpleado.setter
    def idEmpleado(self, valor):
        self.__idEmpleado = valor

    def agregar(self):
        archivo=open("./archivos/Curso.txt", 'a')
        archivo.write(f"{self.idCurso} / {self.descripcion} / {self.idEmpleado} \n")
        archivo.close()

    def borrar(self):
        archivo = open("./archivos/Curso.txt", 'r')
        lineas = archivo.readlines()
        archivo.close()
        archivo = open("./archivos/Curso.txt", 'w')
        for linea in lineas:
             if linea != (f"{self.idCurso} / {self.descripcion} / {self.idEmpleado} \n"):
                archivo.write(linea)
        archivo.close()

    def consultar(self):
        archivo=open("./archivos/Curso.txt", 'r')
        print("\n")
        print (archivo.read())
        archivo.close()