#Classe Forma Geométrica
class Forma():
  def calculaArea(self):
    pass


#Classe Quadrado
class Quadrado(Forma):
  def __init__(self,base):    
    self.base = base

  def calculaArea(self):      
    return self.base * self.base


#Classe Circulo
class Circulo(Forma):
  def __init__(self, raio):
    self.raio = raio

  def calculaArea(self):
    return self.raio * self.raio * 3.14