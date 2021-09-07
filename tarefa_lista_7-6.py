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

class AtualizadorDeContas:
    def __init__(self,selic,saldo_total):
        self.selic=selic
        self.saldo_total=saldo_total

    def roda(self,conta):
        print(conta.saldo)
        conta.atualiza(self.selic)
        print(conta.saldo)
        self.saldo_total+=conta.saldo

c = Conta('123-4', 'Joao', 1000.0)
cc = ContaCorrente('123-5', 'José', 1000.0)
cp = ContaPoupanca('123-6', 'Maria', 1000.0)

adc = AtualizadorDeContas(0.01,0)

sair=1
while(sair):
    menu=input("Selecione uma opção:\n1.Exibir saldos\n2.Depositar\n3.Atualizar contas\n4.Exibir saldo total\n0.Sair\n")
    if(menu=='1'):
        print(f"{c.nome}: R${c.saldo}\n{cc.nome}: R${cc.saldo}\n{cp.nome}: R${cp.saldo}\n")
    elif(menu=='2'):
        menu=input("Escolha o destinatário:\n1.João\n2.José\n3.Maria\n")
        valor=float(input("Digite o valor a ser depositado: "))
        if(menu=='1'):
            c.deposita(valor)
        elif(menu=='2'):
            cc.deposita(valor)
        elif(menu=='3'):
            cp.deposita(valor)
        else:
            print("\nOpção inválida.")
    elif(menu=='3'):
        adc.saldo_total=0.
        adc.roda(c)
        adc.roda(cc)
        adc.roda(cp)
    elif(menu=='4'):
        print('Saldo total: {}'.format(adc.saldo_total))
    elif(menu=='0'):
        sair=0
    else:
        print("\nOpção inválida.")