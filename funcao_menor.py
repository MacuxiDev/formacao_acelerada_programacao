def acha_menor(n1, n2, n3):
    menor = n1  # Inicializa o menor com o primeiro número. Var. Local
    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3
    return menor

#-----------CODIGO PRINCIPAL -----------
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
c = float(input("Digite o terceiro número: "))


menor_todos = acha_menor(a, b, c)    

 
print(f"O menor número é: {menor_todos}")