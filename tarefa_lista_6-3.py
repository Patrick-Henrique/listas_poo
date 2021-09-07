class Atleta:
    def __init__(self,aposentado,peso):
        self.aposentado=aposentado
        self.peso=peso
    
    def aposentar(self):
        print("\nFim de carreira\n")
        self.aposentado=True

    def aquecer(self):
        pass

class Corredor(Atleta):
    def __init__(self,aposentado,peso):
        super() .__init__(aposentado,peso)

    def aquecerCorrida(self):
        print("Aquecendo para correr...\n")

class Nadador(Atleta):
    def __init__(self,aposentado,peso):
        super() .__init__(aposentado,peso)

    def aquecerNado(self):
        print("Aquecendo para nadar...\n")

class Ciclista(Atleta):
    def __init__(self,aposentado,peso):
        super() .__init__(aposentado,peso)
    
    def aquecerCiclismo(self):
        print("Aquecendo para pedalar...\n")

class TriAtleta(Corredor,Nadador,Ciclista):
    def __init__(self,aposentado,peso):
        super() .__init__(aposentado,peso)

sair=1
triGuri=TriAtleta(False,60)
while(sair):
    menu=input("Escolha a ação:\n1.Aquecer\n2.Aposentar\nOutros: sair\n")
    if(menu=='1'):
        menu=input("Aquecer qual modalidade: 1.Corrida | 2.Natação | 3.Ciclismo?\n")
        if(menu=='1'):
            triGuri.aquecerCorrida()
        elif(menu=='2'):
            triGuri.aquecerNado()
        elif(menu=='3'):
            triGuri.aquecerCiclismo()
        else:
            print("\nOpção inválida.")
    elif(menu=='2'):
        triGuri.aposentar()
        sair=0
    else:
        print("\nOpção inválida.")
print("\nAté mais!")      