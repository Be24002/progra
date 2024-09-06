import math
print("Declarar variables para el P1(x1,y1,z1), P2(x2,y2,z2) y p3(x3,y3,z3)")

print("ingrese coordenadas para el primer punto en el espacio")
x1= float(input("x1=\n"))
y1= float(input("y1=\n"))
z1= float(input("z1=\n"))
print("ingrese coordenadas para el segundo punto en el espacio")
x2= float(input("x2=\n"))
y2= float(input("y2=\n"))
z2= float(input("z2=\n"))
print("ingrese coordenadas para el tercer punto en el espacio")
x3= float(input("x3=\n"))
y3= float(input("y3=\n"))
z3= float(input("z3=\n"))
a= math.sqrt((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)
b= math.sqrt((x3-x2)**2+(y3-y2)**2+(z3-z2)**2)
c= math.sqrt((x1-x3)**2+(y1-y3)**2+(z1-z3)**2)
S= (a+b+c)/2
# operacion
area= math.sqrt(S*(S-a)*(S-b)*(S-c))


print(f"el area del triangulo es:{area}")
