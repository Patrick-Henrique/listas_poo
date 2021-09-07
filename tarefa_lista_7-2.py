class Conta:
    def __init__(self,cpf,nome,saldo):
        self.cpf=cpf
        self.nome=nome
        self.saldo=saldo
    
    def deposita(self,valor):
        self.saldo+=valor

    def atualiza(self,taxa):
        self.saldo+=self.saldo*taxa