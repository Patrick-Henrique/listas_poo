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

c=Conta('123-4','Joao',1000.0)
cc=ContaCorrente('123-5','Jose',1000.0)
cp=ContaPoupanca('123-6','Maria',1000.0)

c.atualiza(0.01)
cc.atualiza(0.01)
cp.atualiza(0.01)

print(c.saldo)
print(cc.saldo)
print(cp.saldo)