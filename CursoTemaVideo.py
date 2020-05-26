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