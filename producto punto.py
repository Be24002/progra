import math

print("Encontrar el angulo de la suma de vectores A y B")

Ax= float(input("coordenada de A en x=\n"))
Ay= float(input("coordenada de A en y=\n"))
Az= float(input("coordenada de A en z=\n"))
Bx= float(input("coordenada de B en x=\n"))
By= float(input("coordenada de B en y=\n"))
Bz= float(input("coordenada de B en z=\n"))

A= math.sqrt((Ax)**2+(Ay)**2+(Az)**2)
B= math.sqrt((Bx)**2+(By)**2+(Bz)**2)

x= ((Ax*Bx)+(Ay*By)+(Az*Bz))/(A*B)

# operaciones

theta = math.acos(x)

#  Resultado de la operacion

print(f"el angulo de ambos vectores es:{math.degrees(theta)} grados")
