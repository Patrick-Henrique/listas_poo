import os
class Veiculo:
    def __init__(self,modelo,ano,qtde_litros_no_tanque):
        self.__modelo=modelo
        self.__ano=ano
        self.__qtde_litros_no_tanque=qtde_litros_no_tanque

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    def modelo(self,modelo):
        self.__modelo=modelo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self,ano):
        self.__ano=ano

    @property
    def qtde_litros_no_tanque(self):
        return self.__qtde_litros_no_tanque
    
    @qtde_litros_no_tanque.setter
    def qtde_litros_no_tanque(self,qtde):
        self.__qtde_litros_no_tanque=qtde

    def abastecer(self,qtde_abastecer):
        self.__qtde_litros_no_tanque+=qtde_abastecer

sair=1
while(sair):
    menu=input("Escolha uma ação:\n1.Criar/recriar um carro\n2.Alterar modelo\n3.Alterar ano\n4.Alterar quantidade no tanque\n5.Abastecer\n6.Exibir informações\n7.Conclusão sobre a questão 8.5\n0.Sair\n")
    if(menu=='1'):
        modelo=str(input("Digite o modelo: "))
        ano=str(input("Digite o ano: "))
        carro=Veiculo(modelo,ano,0)
    elif(menu=='2'):
        modelo=input("Digite o novo modelo: ")
        carro.modelo=modelo
    elif(menu=='3'):
        ano=input("Digite o novo ano: ")
        carro.ano=ano
    elif(menu=='4'):
        qtde_abastecer=float(input("Digite a quantidade nova no tanque: "))
        carro.qtde_litros_no_tanque=qtde_abastecer
    elif(menu=='5'):
        qtde_abastecer=float(input("Digite a quantidade de litros para abastecer: "))
        carro.abastecer(qtde_abastecer)
    elif(menu=='6'):
        print(f"\nModelo: {carro.modelo}\nAno: {carro.ano}\nCombustível no tanque: {carro.qtde_litros_no_tanque} litros.")
    elif(menu=='7'):
        os.system("cls")
        print('Se não usar @property e tentar acessar o método getter, como sugerido na questão, um erro ocorre na exibição e não mostra o valor.')
    elif(menu=='0'):
        sair=0
    else:
        print("\nOpção inválida.")