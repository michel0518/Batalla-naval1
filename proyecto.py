import random

def crearTablero(tamano):
    return [["~" for _ in range(tamano)]for _ in range(tamano)]

def mostrarTableros (tableroDisparosjugador,tableroDisparosoponente):
    print("tu tablero de disparos: ")
    for fila in tableroDisparosjugador:
        print(" ".join(fila))
    
    print("tablero disparos del oponente: ")
    for fila in tableroDisparosoponente:
        print(" ".join(fila))


def colocarBarcos(tablero, barcos, jugador):
    for barco in barcos:
        colocado=False
        while not colocado:
            if jugador =="jugador":
               print (f"colocando{barco['nombre']}de tamano{barco['tamano']}")
               fila= int(input("ingresa la fila"))
               columna=int(input("ingrese la columna"))
               orientacion=input("ingrsar la orientacion (h para hotizontal, v para vertical): " ).lower
            else:
                fila=random.randint(0, len(tablero)-1)
                columna=random.randint(0, len(tablero)-1)
                orientacion=random.choice(['h','v'])
            if validarColocacion(tablero,fila,columna,barco['tamano'],orientacion):
                colocarBarco(tablero,fila,columna,barco['tamano'],orientacion)
                colocado=True
            elif jugador=="jugador":
                print("colocacion invalidad. intentalo de nuevo")

def validarColocacion(tablero, fila, columna, tamano, orientacion):
    if orientacion== 'h' :
        if columna+tamano> len(tablero):
             return False
        for i in range (tamano):
            if tablero[fila][columna+i]!= "~":
                return False
    else:
        if fila + tamano > len (tablero):
            return False
        for i in range (tamano):
            if tablero[fila+i][columna]!= "~":
               return False    

    return True

def colocarBarco(tablero, fila, columna, tamano, orientacion):
    if orientacion == 'h':
        for i in range(tamano):
            tablero[fila][columna + i] = "B"
    else:
        for i in range(tamano):
            tablero[fila + i][columna] = "B"

def realizarDisparo(tableroOculto, tableroDisparos, fila, columna):
    if tableroOculto[fila][columna] == "B":
        tableroDisparos[fila][columna] = "X"
        tableroOculto[fila][columna] = "H"  # Marcar como hundido
        return "Impacto"
    elif tableroDisparos[fila][columna] == "~":
        tableroDisparos[fila][columna] = "O"
        return "Agua"
    return "Ya disparaste aquí"

def verificarVictoria(tableroOculto):
    for fila in tableroOculto:
        if "B" in fila:  # Si hay algún barco no hundido
            return False
    return True


def jugarContracomputador ():
    tamano=5
    tablerojugador=crearTablero(tamano)
    tableroComputadora=crearTablero(tamano)
    tableroDisparosJugador=crearTablero(tamano)
    tableroDisparosComputadora=crearTablero(tamano)

    barcos=[
        {"nombre": "portaaviones", "tamano":3},
        {"nombre": "submarino", "tamano":2}
    ]        

    print("Coloca tus barcos")
    colocarBarcos(tablerojugador,barcos,"jugador")
    colocarBarcos(tableroComputadora,barcos,"computadora")

    turnoJugador=True

    while True:
        if turnoJugador:
            print("Tu turno")
            mostrarTableros(tableroDisparosJugador,tableroDisparosComputadora)
            fila= int (input("Ingresa fila de disparo: "))
            columna=int(input("Ingresa columna de disparo: "))
            resultado= realizarDisparo(tableroComputadora,tableroDisparosJugador,fila,columna)
            print(resultado)
            if verificarVictoria (tableroComputadora):
                print ("¡ganaste!")
                return "jugador"

        else:
           print("Turno de la computadora")
           fila=random.randint(0,tamano-1)
           columna=random.randint(0,tamano-1)
           resultado=realizarDisparo(tablerojugador,tableroDisparosComputadora,fila,columna)
           print (f"la computadora disparo en ({fila},{columna}):{resultado}")
           if verificarVictoria(tablerojugador):
               print("la computadora gano.") 
               return "computadora"
           
        turnoJugador=not turnoJugador


def jugarDosjugadores():
    tamano = 5
    tableroJugador1=crearTablero(tamano)
    tableroJugador2=crearTablero(tamano)
    tableroDisparosJugador1=crearTablero(tamano)
    tableroDisparosJugador2=crearTablero(tamano)

    barcos=[
        {"nombre": "portaaviones", "tamano":3},
        {"nombre": "submarino", "tamano":2}
    ]        
    print("Jugador 1 coloca sus barcos")
    colocarBarcos(tableroJugador1,barcos,"jugador")
    print("Jugador 2 coloca sus barcos")
    colocarBarcos(tableroJugador2,barcos,"jugador")

    turnoJugador1=True
    while True:
            if turnoJugador1:
                print ("Turno del jugar 1")
                mostrarTableros(tableroDisparosJugador1,tableroDisparosJugador2)
                fila=int (input("ingresa la fila del disparo: "))
                columna=int (input("ingresa la columna de disparo: "))
                resultado=realizarDisparo(tableroJugador2,tableroDisparosJugador1,fila,columna)
                print (resultado)
                if verificarVictoria(tableroJugador2):
                    print("¡Jugador 1 gano!") 
                    return "jugador 1"
            else:
                print("Turno jugador2")
                mostrarTableros(tableroDisparosJugador2,tableroDisparosJugador1)
                fila=int (input("ingresa la fila del disparo"))
                columna=int (input("ingresa la columna de disparo"))
                resultado=realizarDisparo(tableroJugador1,tableroDisparosJugador2,fila,columna)
                print (resultado)
                if verificarVictoria(tableroJugador1):
                    print("¡Jugador 2 gano!") 
                    return "jugador 2"
            turnoJugador1=not turnoJugador1

def mostrarMenu():
    print("Bienvenido al juego Batalla naval")
    print("1. juega contra la computadora")
    print("2. Dos jugadores")
    print("3. Salir")

def iniciarJuego():
    while True:
        mostrarMenu()
        modo= input ("Elige una opcion")

        if modo =="1":
            ganador= jugarContracomputador()

        elif modo== "2":
            ganador=jugarDosjugadores()

        elif modo== "3":
            print("Gracias por jugar. ¡hasta pronto!")
            break
        else:
            print("la opcion seleccionada no es valida, elige una opcion entre 1 y 3")
            continue
        print(f"El ganador es {ganador}: ")

        jugarDenuevo=input("¿Quiere jugar de nuevo? (s/n): ").lower()
        if jugarDenuevo!= "s":
            print("Gracias por jugar. ¡Hasta la proxima!")
            break
iniciarJuego()