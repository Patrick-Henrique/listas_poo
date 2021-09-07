class Conta:
    def __init__(self,cpf,nome,saldo,numero_alteracoes):
        self.__cpf=cpf
        self.__nome=nome
        self.__saldo=saldo
        self.__numero_alteracoes=numero_alteracoes

    def deposita(self,valor):
        self.__saldo+=valor

    @property
    def getCPF(self):
        return self.__cpf

    def setCPF(self,cpf):
        self.__cpf=cpf

    @property
    def getNome(self):
        return self.__nome

    def setNome(self,nome):
        self.__nome=nome

    @property
    def getNumeroAlteracoes(self):
        return self.__numero_alteracoes

    def setNumeroAlteracoes(self):
        self.__numero_alteracoes+=1