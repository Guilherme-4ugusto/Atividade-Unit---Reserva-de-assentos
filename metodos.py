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

def cadastrar_clientes():
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o CPF do cliente: ")
    with open("clientes.txt", "a") as arquivo:
        arquivo.write(nome + "," + cpf + "\n")

def consultar_cliente():
    cpf_consulta = input("Digite o CPF do cliente que deseja consultar: ")
    encontrado = False
    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            nome, cpf = linha.strip().split(",")
            if cpf == cpf_consulta:
                print("Cliente encontrado:")
                print("Nome:", nome)
                print("CPF:", cpf)
                encontrado = True
                break
    if not encontrado:
        print("Cliente não encontrado.")

def relatorio_reservas():
    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()