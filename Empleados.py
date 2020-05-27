class empleado:
    
    def __init__(self, idempleado, nombre, direccion):
        self.idempleado = idempleado
        self.nombre = nombre
        self.direccion = direccion

    @property
    def idempleado(self):
        return self.__idempleado

    @idempleado.setter
    def idempleado(self, valor):
        self.__idempleado = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direccion(self, valor):
        self.__direccion = valor

    def agregar(self):
        archivo=open("./archivos/Empleado.txt", 'a')
        archivo.write(f"{self.idempleado} / {self.nombre} / {self.direccion} \n")
        archivo.close()

    def borrar(self):
        archivo = open("./archivos/.Empleadotxt", 'r')
        lineas = archivo.readlines()
        archivo.close()
        archivo = open("./archivos/Empleado.txt", 'w')
        for linea in lineas:
             if linea != (f"{self.idempleado} / {self.nombre} / {self.direccion} \n"):
                archivo.write(linea)
        archivo.close()

    def consultar(self):
        archivo=open("./archivos/Empleado.txt", 'r')
        print("\n")
        print (archivo.read())
        archivo.close()