a = 0
b = 0
c = 0

a = int(input("Digite um numero 1\n"))
b = int(input("Digite um numero 2\n"))
c = int(input("Digite um numero 3\n"))

if(a < b < c):
    print("Numero 1 é menor")
elif(b < a < c):
    print("Numero 2 é menor")
else:
    print("numero 3  e menor")        