x=float(input("ingrese un valor"))
term=1
suma=0
n=0
epsilon= 1e-15
while abs(term)>=epsilon:

     suma=suma+term
     n=n+1
     fact=1
     i=1
     while (i<=n):
            fact=fact*i
            i=i+1
     term=pow(x,n)/fact
        
print(f"el valor de la suma es:{suma}")
print(f"{n-1}")
