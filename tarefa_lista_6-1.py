class Ingresso:
    def __init__(self,valorEmReais):
        self.valorEmReais=valorEmReais
    
    def imprimeValor(self):
        return print(f"Valor do ingresso: R${self.valorEmReais}")

class VIP(Ingresso):
    def __init__(self,valorEmReais,adicional):
        super() .__init__(valorEmReais)
        self.adicional=adicional
    
    def imprimeValor(self):
        return print(f"Valor do ingresso: R${self.valorEmReais}")

bilhetenormal=Ingresso(50)
adicional=30

sair=1
while(sair):
    menu=input("Escolha uma opção:\n1.Exibir valor ingresso normal\n2.Exibir valor ingresso VIP\n3.Alterar valor ingresso normal\n4.Alterar valor adicional\nOutros: sair\n")
    if(menu=='1'):
        bilhetenormal.imprimeValor()
    elif(menu=='2'):
        bilheteVIP=VIP(bilhetenormal.valorEmReais+adicional,adicional)
        bilheteVIP.imprimeValor()
    elif(menu=='3'):
        bilhetenormal.valorEmReais=float(input("Digite o novo valor: "))
    elif(menu=='4'):
        adicional=float(input("Digite o novo adicional de ingresso VIP: "))
    else:
        sair=0