print("calcular la pendiente y el intersecto de la funcion")
      
#variables

x1= float(input("punto x1=\n"))
y1= float(input("punto y1=\n"))
x2= float(input("punto x2=\n"))
y2= float(input("punto y2=\n"))

# operacioness

m=(y2-y1)/(x2-x1)
b= y1-m*x1

# 
print(f"la pendiente y el intersecto es:{m},{b}")
