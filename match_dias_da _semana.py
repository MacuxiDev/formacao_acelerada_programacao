def verificar_dia_util(dia):
    match dia:
        case 'segunda' | 'terca' | 'quarta' | 'quinta' | 'sexta':
            return 'Dia da Semana'
        case 'sabado' | 'domingo':
            return 'Final de Semana'
        case _:
            return 'Dia inválido'

dia = input('Diga o dia\n')
print(verificar_dia_util(dia))