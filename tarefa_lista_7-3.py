class Conta:
    def __init__(self,cpf,nome,saldo):
        self.cpf=cpf
        self.nome=nome
        self.saldo=saldo
    
    def deposita(self,valor):
        self.saldo+=valor

    def atualiza(self,taxa):
        self.saldo+=self.saldo*taxa
    
class ContaCorrente(Conta):
    def __init__(self,cpf,nome,saldo):
        super() .__init__(cpf,nome,saldo)

    def atualiza(self,taxa):
        self.saldo+=self.saldo*taxa*2

    def deposita(self,valor):
        self.saldo+=valor-0.1

class ContaPoupanca(Conta):
    def __init__(self,cpf,nome,saldo):
        super() .__init__(cpf,nome,saldo)
    
    def atualiza(self,taxa):
        self.saldo+=self.saldo*taxa*3