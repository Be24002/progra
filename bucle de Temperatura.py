repetir= 1
while(repetir==1): 
    Tcel=float(input("ingrese temperatura en celcius"))
    if Tcel >= -273.15:
        repetir= 0
    else:
        print("la temperatura en celcius debe ser mayor que -273.15")

Tfah= (1.8*Tcel)+32

print(f"C equivale a:{Tfah}")
