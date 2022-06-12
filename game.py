import pandas as pd
import sys
import itertools

while True:
    print("**********************")
    print("* Talana Kombat JRPG *")
    print("**********************")
    print("Tenemos 3 combates")
    print("combate1")
    print("combate2")
    print("combate3")

    json = input('¿Qué combate prefieres? o escribe exit para salir >>> ')
    json = json.lower()
    if (json != "exit"):
        try:
            #Convertimos Json a Dataframe
            df = pd.read_json(json+'.json')

            #Golpes de personajes
            mov1_j1 = ["DSDP", 3, "Taladoken"]
            mov2_j1 = ["SDK", 2, "Remuyuken"]
            mov3_j1 = ["P", 1, "Puñetazo"]
            mov4_j1 = ["K", 1, "Patada"]

            mov1_j2 = ["SAK", 3, "Remuyuken"]
            mov2_j2 = ["ASAP", 2, "Taladoken"]
            mov3_j2 = ["P", 1, "Puño"]
            mov4_j2 = ["K", 1, "Patada"]

            #Obtenemos los movimientos y golpes de cada jugador, los almacenamos en una lista
            movimientos_j1 = (df.loc[["movimientos"], "player1"][0])
            golpes_j1 = (df.loc[["golpes"], "player1"][0])

            movimientos_j2 = (df.loc[["movimientos"], "player2"][0])
            golpes_j2 = (df.loc[["golpes"], "player2"][0])

            com_j1 = []
            com_j2 = []

            #Creamos lista de movimientos Jugador 1
            for valor_a, valor_b, valor_c, valor_d in itertools.zip_longest(movimientos_j1, golpes_j1, movimientos_j2, golpes_j2):
                if(valor_a == None):
                    valor_a = ""
                if(valor_b == None):
                    valor_b = ""
                if(valor_c == None):
                    valor_c = ""
                if(valor_d == None):
                    valor_d = ""
                #Limitar un máximo de 5 Movimientos y 1 Golpe
                if(len(valor_a) < 6 and len(valor_b) < 2):
                    com_j1 += [(str(valor_a + valor_b))]
                #En caso contrario, dejo en blanco
                else:
                    com_j1 += [""]
                #Limitar un máximo de 5 Movimientos y 1 Golpe
                if(len(valor_c) < 6 and len(valor_d) < 2):
                    com_j2 += [(str(valor_c + valor_d))]
                #En caso contrario, dejo en blanco
                else:
                    com_j2 += [""]

            #¿Quién Comienza?
            if(len(com_j1[0]) < len(com_j2[0])):
                p = 1
            elif(len(com_j2[0]) < len(com_j1[0])):
                p = 2
            elif(len(movimientos_j1[0]) < len(movimientos_j2[0])):
                p = 1
            elif(len(movimientos_j2[0]) < len(movimientos_j1[0])):
                p = 2
            elif(len(movimientos_j1[0]) < len(movimientos_j2[0])):
                p = 1
            elif(len(movimientos_j2[0]) < len(movimientos_j1[0])):
                p = 2
            else:
                p = 1

            #Recargamos Vida
            player1 = [6, "Tonyn"]
            player2 = [6, "Arnaldor"]

            #Creamos las funciones de la pelea
            def MovimientoJugador1(valor_a):
                if(valor_a == mov1_j1[0]):
                    player2[0] = player2[0] - mov1_j1[1]
                    print(player1[1]+" usa un "+ mov1_j1[2])
                elif(valor_a == mov2_j1[0]):
                    player2[0] = player2[0] - mov2_j1[1]
                    print(player1[1]+" conecta un "+ mov2_j1[2])
                elif(valor_a == mov3_j1[0]):
                    player2[0] = player2[0] - mov3_j1[1]
                    print(player1[1]+" le da un "+ mov3_j1[2] + " al pobre " + player2[1])
                elif(valor_a == mov4_j1[0]):
                    player2[0] = player2[0] - mov4_j1[1]
                    print(player1[1]+" le da una "+ mov4_j1[2] + " al pobre " + player2[1])
                else:
                    if(len(valor_a) > 0):
                        if(len(valor_a) == 2 and valor_a[1] == "P" and valor_a[0] == "D"):
                            player2[0] = player2[0] - mov3_j1[1]
                            print(player1[1]+" avanza y dá un "+mov3_j1[2])
                        elif(len(valor_a) == 2 and valor_a[1] == "K" and valor_a[0] == "D"):
                            player2[0] = player2[0] - mov3_j1[1]
                            print(player1[1]+" avanza y dá una "+mov4_j1[2])
                        elif(valor_a[(len(valor_a)-1)] == "P"):
                            player2[0] = player2[0] - mov3_j1[1]
                            print(player1[1]+" se mueve y dá un "+mov3_j1[2])
                        elif(valor_a[(len(valor_a)-1)] == "K"):
                            player2[0] = player2[0] - mov3_j1[1]
                            print(player1[1]+" se mueve y dá una "+mov4_j1[2])
                        else:
                            print(player1[1]+" se mueve")
                    else:
                            print(player1[1]+" no hace nada")

                

            def MovimientoJugador2(valor_b):
                if(valor_b == mov1_j2[0]):
                    player1[0] = player1[0] - mov1_j2[1]
                    print(player2[1]+" conecta un "+ mov1_j2[2])
                elif(valor_b == mov2_j2[0]):
                    player1[0] = player1[0] - mov2_j2[1]
                    print(player2[1]+" usa un "+ mov2_j2[2])
                elif(valor_b == mov3_j2[0]):
                    player1[0] = player1[0] - mov3_j2[1]
                    print(player2[1]+" le da un "+ mov3_j2[2] + " al pobre " + player1[1])
                elif(valor_b == mov4_j2[0]):
                    player1[0] = player1[0] - mov4_j2[1]
                    print(player2[1]+" le da una "+ mov4_j2[2] + " al pobre " + player1[1])
                else:
                    if(len(valor_b) > 0):
                        if(len(valor_b) == 2 and valor_a[1] == "P" and valor_a[0] == "A"):
                            player1[0] = player1[0] - mov3_j2[1]
                            print(player2[1]+" avanza y dá un "+mov3_j2[2])
                        elif(len(valor_b) == 2 and valor_a[1] == "K" and valor_a[0] == "A"):
                            player1[0] = player1[0] - mov4_j2[1]
                            print(player2[1]+" avanza y dá una "+mov4_j2[2])
                        elif(valor_b[(len(valor_b)-1)] == "P"):
                            player1[0] = player1[0] - mov3_j2[1]
                            print(player2[1]+" se mueve y dá un "+mov3_j2[2])
                        elif(valor_b[(len(valor_b)-1)] == "K"):
                            player1[0] = player1[0] - mov4_j2[1]
                            print(player2[1]+" se mueve y dá una "+mov4_j2[2])
                        else:
                            print(player2[1]+" se mueve")
                    else:
                            print(player2[1]+" no hace nada")        

            #Progreso de Vida de nuestros jugadores
            def progress(count, total, status='', bar_len=60):
                filled_len = int(round(bar_len * count / float(total)))

                percents = round(100.0 * count / float(total), 1)
                bar = '=' * filled_len + '-' * (bar_len - filled_len)

                fmt = '[%s] %s%s ...%s' % (bar, percents, '%', status)
                print('\b' * len(fmt), end='')  # clears the line
                sys.stdout.write(fmt)
                sys.stdout.flush()

            #Iniciamos Combate
            for valor_a, valor_b in zip(com_j1, com_j2):
                if(p == 1):
                    MovimientoJugador1(valor_a)
                    MovimientoJugador2(valor_b)
                else:
                    MovimientoJugador2(valor_b)
                    MovimientoJugador1(valor_a)

                if(player1[0] <= 0):
                    ganador = (player2[1] + " Gana la pelea y aun le queda "+ str(player2[0]) + " de energía")
                    print(ganador)
                    print(player2[1] + str(progress(player2[0], 6)))
                    print(player1[1] + str(progress(0, 6)))
                    break

                if(player2[0] <= 0):
                    ganador = (player1[1] + " Gana la pelea y aun le queda "+ str(player1[0]) + " de energía")
                    print(ganador)
                    print(player1[1] + str(progress(player1[0], 6)))
                    print(player2[1] + str(progress(0, 6)))
                    break
        except:
            print("Aprovechen el Bug y vuelvan a Intentarlo xD")
    elif (json == "exit"):
        break
