import math
# Entrada 
x1 = 0
y1 = 0

x2 = int(input("Ingrese la coordenada en el eje x\n"))
y2 = int(input("Ingrese la coordenada en el eje y\n"))

coordenada = [x2,y2]

# Proceso

distancia = math.sqrt(math.pow((x2 - x1)*(x2 - x1),2) + math.pow((y2 - y1)*(y2 - y1),2)) 

print ("Coordenada :", coordenada)
print("La distancia entre [0,0] y ", coordenada, " es :", round(distancia))
