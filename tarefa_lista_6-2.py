import os

class Forma:
    def __init__(self,area,perimetro):
        self.area=area
        self.perimetro=perimetro
    
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

class Retangulo(Forma):
    def __init__(self,area,perimetro):
        super() .__init__(area,perimetro)
    
    def calcularArea(self,base,altura):
        return base*altura
    
    def calcularPerimetro(self,base,altura):
        return (2*base+2*altura)

class Triangulo(Forma):
    def __init__(self,area,perimetro,altura):
        super() .__init__(area,perimetro)
        self.altura=altura

    def calcularArea(self,altura):
        return ((pow(altura,2)*pow(3,0.5))/3)
    def calcularPerimetro(self,altura):
        return (2*altura*pow(3,0.5))

sair=1
area=1.
perimetro=1.
altura=1.
while(sair):
    menu=input("Escolha uma opção:\n1.Calcular área e perímetro do retângulo\n2.Calcular área e perímetro do triângulo\nOutros: sair\n")
    if(menu=='1'):
        base=float(input("Digite a medida da base: "))
        altura=float(input("Digite a medida da altura: "))
        ret1=Retangulo(area,perimetro)
        ret1.area=ret1.calcularArea(base,altura)
        ret1.perimetro=ret1.calcularPerimetro(base,altura)
        print(f"\nÁrea: {ret1.area}\nPerímetro: {ret1.perimetro}\n")
    elif(menu=='2'):
        altura=float(input("Digite a altura do triângulo equilátero: "))
        tri1=Triangulo(area,perimetro,altura)
        tri1.area=tri1.calcularArea(altura)
        tri1.perimetro=tri1.calcularPerimetro(altura)
        print(f"\nÁrea: {tri1.area}\nPerímetro: {tri1.perimetro}\n")
    else:
        sair=0