def relatorio_reservas():
    with open("reservas.txt", "r") as arquivo:
        reservas = arquivo.readlines()
