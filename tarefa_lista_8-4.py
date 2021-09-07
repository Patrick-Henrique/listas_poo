class Veiculo:
    def __init__(self,modelo,ano,qtde_litros_no_tanque):
        self.__modelo=modelo
        self.__ano=ano
        self.__qtde_litros_no_tanque=qtde_litros_no_tanque

    def getModelo(self):
        return self.__modelo

    def setModelo(self,modelo):
        self.__modelo=modelo

    def getAno(self):
        return self.__ano

    def setAno(self,ano):
        self.__ano=ano

    def getQtde(self):
        return self.__qtde_litros_no_tanque
    
    def setQtde(self,qtde):
        self.__qtde_litros_no_tanque=qtde

    def abastecer(self,qtde_abastecer):
        self.__qtde_litros_no_tanque+=qtde_abastecer