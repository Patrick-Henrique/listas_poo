class Conta:
    def __init__(self,nome_titular,cpf,saldo):
        self.nome_titular=nome_titular
        self.cpf=cpf
        self.saldo=saldo
    
    def consultaSaldo(self):
        return print(f"Saldo: {self.saldo}")

    def adicionar_juros(self):
        pass

class Poupanca(Conta):
    def __init__(self,nome_titular,cpf,saldo):
        super() .__init__(nome_titular,cpf,saldo)

    def adicionar_juros(self,meses):
        self.saldo*= 1+meses*0.005
        return self.saldo

sair=1
cliente=Conta("Tiburcio","123.456.789-01",1000)
contaP=Poupanca(cliente.nome_titular,cliente.cpf,cliente.saldo)
cliente.saldo=contaP.saldo
while(sair):
    cliente.saldo=contaP.saldo
    menu=input("Escolha uma opção:\n1.Exibir saldo atual\n2.Adicionar meses ao saldo\nOutros: sair\n")
    if(menu=='1'):
        cliente.consultaSaldo()
    elif(menu=='2'):
        meses=int(input("Digite o número de meses para render a poupança: "))
        contaP.saldo=contaP.adicionar_juros(meses)
    else:
        sair=0