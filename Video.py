class video:

    def __init__(self, idVideo, nombre, url, fechapublicacion):
        self.idVideo = idVideo
        self.nombre = nombre
        self.url = url
        self.fechapublicacion = fechapublicacion
    
    @property
    def idVideo(self):
        return self.__idVideo

    @idVideo.setter
    def idVideo(self, valor):
        self.__idVideo = valor

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        self.__nombre = valor

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, valor):
        self.__url = valor

    @property 
    def fechapublicacion(self):
        return self.__fechapublicacion

    @fechapublicacion.setter
    def fechapublicacion(self, valor):
        self.__fechapublicacion = valor

    def agregar(self):
        archivo=open("./archivos/video.txt", 'a')
        archivo.write(f"{self.idVideo} / {self.nombre} / {self.url} / {self.fechapublicacion} \n")
        archivo.close()

    def borrar(self):
        archivo = open("./archivos/video.txt", 'r')
        lineas = archivo.readlines()
        archivo.close()
        archivo = open("./archivos/video.txt", 'w')
        for linea in lineas:
             if linea != (f"{self.idVideo} / {self.nombre} / {self.url} / {self.fechapublicacion} \n"):
                archivo.write(linea)
        archivo.close()

    def consultar(self):
        archivo=open("./archivos/video.txt", 'r')
        print("\n")
        print (archivo.read())
        archivo.close()