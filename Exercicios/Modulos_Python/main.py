import FormaGeometrica.Formas

#Objetos
quadrado1 = FormaGeometrica.Formas.Quadrado(5)
areaQ = quadrado1.calculaArea()

circulo1 = FormaGeometrica.Formas.Circulo(2)
areaC = circulo1.calculaArea()

print("Área Quadrado: " + str(areaQ))
print("Área Circulo: " + str(areaC))