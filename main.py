import metodos

while True:
    opcao = metodos.printarMenu()
    if opcao == 0:
        break
    elif opcao == 1:
        metodos.cadastrar_clientes()
    elif opcao == 2:
        metodos.consultar_cliente()
    elif opcao == 3:
        print("Ainda não suportado")
    elif opcao == 4:
        print("Ainda não suportado")
    elif opcao == 5:
        metodos.relatorio_reservas()
    elif opcao == 6:
        print("Ainda não suportado")
    elif opcao == 7:
        metodos.exibirRelatorioDeCancelamentosDeReservasDeAssentos()
print("O programa foi encerrado!!!")


