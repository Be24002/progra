
epsilon= 1E-15
term=1
m=1
suma= 1

while term>=epsilon:

       suma= suma+term
       m=m+1
       term= 1/(m**2)
print(f"el valor de la suma= {suma}")
print(f"min valor={m-1}")
