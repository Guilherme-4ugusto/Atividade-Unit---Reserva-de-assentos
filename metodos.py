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
    print("\n=========================== Relatorio de reservas canceladas ===========================\n")
    with open("reservas_canceladas.txt", 'r', encoding="utf8") as arq:
        for linha in arq:
            fila, assento, cpf_consulta = linha.strip().split("|")
            with open("clientes.txt", "r") as arquivo:
                for linha in arquivo:
                    nome, cpf = linha.strip().split(",")
                    if cpf == cpf_consulta:
                        print(f"\tA reserva do assento {assento} da fila {fila} vinculado ao cliente {nome} foi cancelada.")
    print("\n========================================================================================\n")

def cadastrar_clientes():
  nome = input("Digite o nome do cliente: ")
  cpf = input("Digite o CPF do cliente: ")
  if not is_cliente_registrado(cpf):
      with open("clientes.txt", "a") as arquivo:
          arquivo.write(nome + "," + cpf + "\n")
          print("Cliente cadastrado!!")
  else:
      print("Cliente ja registrado!!")

def obter_nome_do_cliente_pelo_cpf(cpf):
    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            nome, cpf_consulta = linha.strip().split(",")
            if cpf == cpf_consulta:
                return nome

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
        print("O assento",int(assento)+1,"da fila",int(fila)+1,"está reservado pelo cliente",obter_nome_do_cliente_pelo_cpf(cpf))

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

def relatorio_de_assentos_livres():
    with open("reservas.txt", "r", encoding="utf8") as arquivo:
        reservas = arquivo.readline()
        dadosReservas = reservas.strip().split(",")
    printar_relatorio_de_assentos_livres(dadosReservas)
def printar_relatorio_de_assentos_livres(dadosReservas):
    print("========= Relatorio de assentos livres =========")
    print("\n======== Visão Geral ==================\n")
    print(montaGuiaDaMatriz())
    print_matriz(obterMatrizPreenchida(dadosReservas))
    print("\nX = Reservados | O = Disponíveis")
    print("=======================================")

def reserva_assento():
    cpf_consulta = input("Digite o CPF do cliente a qual a reserva vai ser realizada: ")
    isClienteNaoEncontrado = True
    with open("clientes.txt", "r") as arquivo:
        for linha in arquivo:
            nome, cpf = linha.strip().split(",")
            if cpf == cpf_consulta:
                isClienteNaoEncontrado = False
                fila = int(input("Em qual fila?(1-"+str(FILAS_AVIAO)+") "))
                assento = int(input("Qual assento?(1-"+str(COLUNAS_AVIAO)+") "))
                with open("reservas.txt", "a") as arquivo:
                    if existeRegistrosDeReservas():
                        arquivo.write("," + str(fila-1) + "|" + str(assento-1) + "|" + cpf)
                    else:
                        arquivo.write(str(fila - 1) + "|" + str(assento - 1) + "|" + cpf)
                    print("Reserva realizada!!")
                break
    if(isClienteNaoEncontrado == True):
        print("Cliente não encontrado.")

def existeRegistrosDeReservas():
    with open("reservas.txt", "r") as arquivo:
        if len(arquivo.readlines()) > 0:
            return True
        else:
            return False

def is_cliente_registrado(cpf):
  cpf_consulta = cpf
  encontrado = False
  with open("clientes.txt","r")as arquivo:
    for linha in arquivo:
      nome, cpf = linha.strip().split(",")
      if cpf == cpf_consulta:
        encontrado = True
        return encontrado
        break
      if not encontrado:
        encontrado = False
        return encontrado