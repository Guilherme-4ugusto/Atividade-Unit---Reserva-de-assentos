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