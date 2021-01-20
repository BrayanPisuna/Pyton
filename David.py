N = int (input("Ingrese un numero N: "))
A = [None]*(N+1)
positivos = 0
negativos = 0
ceros = 0
suma = 0
resta= 0
for I in range (1,N+1,1):
    A[I]=int(input("ingrese un numero: "))

for I in range (1,N,1):
    for J in range (I+1,N+1,1):
        if A[J]<A[I]:
            X=A[I]
            A[I]=A[J]
            A[J]=X

print ("lista ordenada: ")
for I in range (1,N+1,1):
    if A[I] > 0:
            positivos += 1
            suma += A[I]
            promedio = suma / positivos 
    elif A[I] < 0:
        negativos += 1
        resta +=  A[I]
    else:
        ceros += 1  
    
    print (A[I])
print ("La cantidad de numeros positivos son:", positivos)      
print ("La cantidad de numeros Negativos son:", negativos)
print ("La cantidad de numeros Ceros son:", ceros)
print ("La suma de los numeros positivos es: ",suma)
print ("El promedio de la suma es: ",promedio)
print ("La suma de los numeros negativos es: ",resta)

