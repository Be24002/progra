repetir= True
while repetir:
    N= int(input("cantidad de datos:"))
    if N>0:
        repetir= False
    else: 
        print(" Cantidad invalida")

i=1
while i<= N:
    Tcel= float(input("ingrese la temperatura en celcius:"))
    if Tcel >= -273.15:
        Tfah= 1.8*Tcel+32
        print(f"{Tcel}C equivalen a {Tfah} F:")
    else:
        print(f"valor de la temperatura celcius incorrecto: {Tcel}")
    i=i+1  
