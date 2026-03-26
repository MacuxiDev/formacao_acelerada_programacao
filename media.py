n1 = 0
n2 = 0
n3 = 0


n1 = float(input('Insira a Nota 1\n'))
n2 = float(input('Insira a Nota 2\n'))
n3 = float(input('Insira a Nota 3\n'))

notas = (n1 + n2 + n3)/3

if(notas >= 7 and notas < 10):
    print("aluno aprovado")
    print(' A media é:',notas)
elif(notas == 10):
    print("aluno aprovado com nota maxima")
    print(' A media é:',notas)
else:
    print("aluno reprovado")
    print(' A media é:',notas)



