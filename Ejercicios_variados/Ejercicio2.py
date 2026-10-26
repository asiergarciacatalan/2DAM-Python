mazo_jugador1 = [2, 4, 6, 8, 10]
mazo_jugador2 = [1,3,5,7,9]

 # Inicializar los mazos con cartas
for i in range(5):
    carta1 = mazo_jugador1.pop(0)
    carta2 = mazo_jugador2.pop(0)

    print(f"Jugador 1 juega: {carta1}")
    print(f"Jugador 2 juega: {carta2}")

    if carta1 > carta2:
        print("Jugador 1 gana la ronda")
        mazo_jugador1.append(carta1)
        mazo_jugador1.append(carta2)
    elif carta2 > carta1:
        print("Jugador 2 gana la ronda")
        mazo_jugador2.append(carta2)
        mazo_jugador2.append(carta1)
    else:
        print("Empate, ambas cartas se descartan")

    print(f"Estado actual del mazo Jugador 1: {mazo_jugador1}")
    print(f"Estado actual del mazo Jugador 2: {mazo_jugador2}")
    print("---------------------------------------------------")

# Ganador
if len(mazo_jugador1) > len(mazo_jugador2):
    print("Jugador 1 gana el juego.")
else:
    print("Jugador 2 gana el juego.")
    