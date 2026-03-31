def verificar_dia_util(dia):
    match dia.lower():
        case "sábado" | "domingo":
            return "Fim de semana!"
        case "segunda" | "terça" | "quarta" | "quinta" | "sexta":
            return "Dia de trabalho."
        case _:
            return "Dia inválido."

input_dia = input("Digite um dia da semana: ")
resultado = verificar_dia_util(input_dia)
print(resultado)
