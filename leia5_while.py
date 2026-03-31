# Lê vários números até que seja digitado 0.
# Exibe a soma e a média dos valores lidos (sem contar o 0 de parada).

soma = 0
quantidade = 0

while True:
    valor = int(input('Digite um número (0 para sair): '))
    if valor == 0:
        break
    soma += valor
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f'Soma: {soma}')
    print(f'Média: {media:.2f}')
else:
    print('Nenhum número válido foi informado.')
