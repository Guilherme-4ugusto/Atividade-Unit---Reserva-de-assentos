FILAS_AVIAO = 8
COLUNAS_AVIAO = 4

def printarMenu():
    print("\n1 - Cadastro de Cliente:")
    print("2 - Consulta de Clientes:")
    print("3 - Reserva de Assento:")
    print("4 - Cancelamento de Reserva de Assento:")
    print("5 - Relatório de Reservas:")
    print("6 - Relatório de Assento Livres:")
    print("7 - Relatório de Cancelamento de Reservas de Assentos:")
    print("0 - Sair")
    return int(input("Informe o número da opção que deseja:"))


def exibirRelatorioDeCancelamentosDeReservasDeAssentos():
    with open("reservas_canceladas", 'r', encoding="utf8") as arq:
        for linha in arq.readlines():

            print(linha.split()[1])
    arq.close()


def cadastrar_clientes():
  nome = input("Digite o nome do cliente: ")
  cpf = input("Digite o CPF do cliente: ")
  with open ("cliente.txt", "a") as arquivo:
      arquivo.write(nome+","+cpf+"\n")
  print("Cliente cadastrado!!")

def obter_nome_do_cliente_pelo_cpf(cpf):
    with open("cliente.txt", "r") as arquivo:
        for linha in arquivo:
            nome, cpf_consulta = linha.strip().split(",")
            if cpf == cpf_consulta:
                return nome

def consultar_cliente():
    cpf_consulta = input("Digite o CPF do cliente que deseja consultar: ")
    encontrado = False
    with open("cliente.txt", "r") as arquivo:
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
    with open("reservas.txt", "r", encoding="utf8") as arquivo:
        reservas = arquivo.readline()
        dadosReserva = reservas.strip().split(",")
    printar_relatorio_de_reservas(dadosReserva)

def printar_relatorio_de_reservas(dadosReserva):
    print("========= Relatorio de reservas =========")
    print("\n======== Visão Geral ==================\n")
    print(montaGuiaDaMatriz())
    print_matriz(obterMatrizPreenchida(dadosReserva))
    print("\nX = Reservados | O = Disponíveis")
    print("=======================================")
    print("\n======== Visão Detalhada ==============")
    for reserva in dadosReserva:
        fila, assento, cpf = reserva.strip().split('|')
        print("O assento",int(assento)+1,"da fila",int(fila)+1,"pelo cliente",obter_nome_do_cliente_pelo_cpf(cpf))

def criamatriz(fila, assento): #Cria matriz com todas as posições com o valor False
    matriz = []
    for i in range (fila):
        linha = []
        for j in range (assento):
            linha.append("O")
        matriz.append(linha)
    return matriz

def print_matriz(matriz):
    for u in range(len(matriz)):
        print(u+1,matriz[u])

def montaGuiaDaMatriz():
    retorno = ""
    for coluna in range(COLUNAS_AVIAO):
        retorno += "    "+str(coluna+1)
    return retorno

def obterMatrizPreenchida(dadosReserva):
    matriz = criamatriz(FILAS_AVIAO, COLUNAS_AVIAO)
    for reserva in dadosReserva:
        fila, assento, cpf = reserva.strip().split('|')
        matriz[int(fila)][int(assento)] = "X"
    return matriz