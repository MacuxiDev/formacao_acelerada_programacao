def comando_servidor(comando):
    match comando:
        case "start":
            return  "Servidor Iniciado"
        case "stop":
            return "Servidor parado"
        case "restart":
            return "Servidor reniciou"
        case _:
            return "Comando não encotrado"
        
comando = input("Digite o comando\n")
print(comando_servidor(comando))

#Exemplo de ultilizacao de match_case e como solicitar ao usuario e a saida do usuario        