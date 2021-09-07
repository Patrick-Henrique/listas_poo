class Conta:
    def __init__(self,cpf,nome,saldo,numero_alteracoes):
        self.__cpf=cpf
        self.__nome=nome
        self.__saldo=saldo
        self.__numero_alteracoes=numero_alteracoes

    def deposita(self,valor):
        self.__saldo+=valor

    def saca(self,valor):
        if(valor>self.__saldo):
            print("\nSaldo insuficiente para a ação.")
        else:
            self.__saldo-=valor

    @property
    def getSaldo(self):
        return self.__saldo

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self,cpf):
        self.__alteracoes()
        self.__cpf=cpf

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__alteracoes()
        self.__nome=nome

    @property
    def numero_alteracoes(self):
        return self.__numero_alteracoes

    
    def __alteracoes(self):
        print("Chegou aqui")
        self.__numero_alteracoes+=1

sair=1
while(sair):
    menu=input("\nEscolha uma ação:\n1.Criar/resetar dados da conta\n2.Alterar nome\n3.Alterar CPF\n4.Exibir número de alterações\n5.Exibir informações da conta\n6.Depositar\n7.Sacar\n0.Sair\n")
    if(menu=='1'):
        nome=str(input("Digite o seu nome: "))
        cpf=str(input("Digite o seu CPF: "))
        saldo=float(input("Digite o seu saldo: "))
        c=Conta(cpf,nome,saldo,0)
    elif(menu=='2'):
        nome=input("Digite o novo nome: ")
        c.nome=nome
    elif(menu=='3'):
        cpf=input("Digite o novo CPF: ")
        c.cpf=cpf
    elif(menu=='4'):
        print(f"Foram feitas {c.numero_alteracoes} alterações na conta.")
    elif(menu=='5'):
        print(f"\nNome: {c.nome}\nCPF: {c.cpf}\nSaldo: {c.getSaldo}\nAlterações na conta: {c.numero_alteracoes}\n")
    elif(menu=='6'):
        valor=float(input("Digite o valor a depositar: "))
        c.deposita(valor)
    elif(menu=='7'):
        valor=float(input("Digite o valor a sacar: "))
        c.saca(valor)
    elif(menu=='0'):
        sair=0
    else:
        print("\nOpção inválida.")