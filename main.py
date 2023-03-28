def relatorio_reservas():
    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()

    print("Relatório de Reservas:")
    for reserva in reservas:
        dados = reserva.strip().split(",")
        print(f"Assento {dados[0]} - Cliente {dados[1]}")