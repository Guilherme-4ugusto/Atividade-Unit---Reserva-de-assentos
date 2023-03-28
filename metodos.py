def printarMenu():
    print("1 - Cadastro de Cliente:")
    print("2 - Consulta de Clientes:")
    print("3 - Reserva de Assento:")
    print("4 - Cancelamento de Reserva de Assento:")
    print("5 - Relatório de Reservas:")
    print("6 - Relatório de Assento Livres:")
    print("7 - Relatório de Cancelamento de Reservas de Assentos:")
    print("0 - Sair")
    return int(input("Informe o número da opção que deseja:"))

def exibirRelatorioDeCancelamentosDeReservasDeAssentos():
    arq = open("reservas_canceladas", 'r', encoding="utf8")
    for linha in arq.readlines():
        print(linha.split())
    arq.close()