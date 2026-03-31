
maior = None
for _ in range(5):
    valor = int(input())
    if maior is None or valor > maior:
        maior = valor
print(maior)