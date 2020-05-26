class Video:
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

    def Agregar(self):
        archivo=open("./archivos/Video.txt", 'a')
        idVideo=(input("Ingresa la id del Video: /n"))
        nombre=(input("Ingrese el nombre del Video: /n"))
        url=(input("Ingrese la url del Video: /n"))
        fechapublicacion=(input("Ingrese la Fecha de Publicación del Video: /n"))
        archivo=write(f"{self.idVideo} / {self.nombre} / {self.url} {self.fechapublicacion} \n")
        archivo.close()
        
        


