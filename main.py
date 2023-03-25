import metodos

opcao = 0;
isPrimeiraExecucao = True

while opcao != 0 or isPrimeiraExecucao:
    isPrimeiraExecucao = False
    opcao = metodos.printarMenu()
    if opcao == 1:
        cadastro = metodos.cadastrar_clientes()
    elif opcao == 2:
        consulta = metodos.consultar_cliente()
