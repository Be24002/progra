#Convertir la temperatura de grados celcius a farenheit
Tcel= float(input("ingrese el valor en grados celcius:\n"))
Celmin= -273.16
if Tcel >= Celmin:
    Tfa= 1.8*Tcel+32
    print(f"{Tcel}°C equivalen a {Tfa})°F")

else:
    print(f" valor de temperatura invalida")
    print(f"El valor minimo de grados celsius es:{Celmin}")
    print(f"\t... Usted ingreso: {Tcel}")
