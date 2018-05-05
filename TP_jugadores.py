from TP_general import solicitarValor

def ingresarNombrePersonas(cant_personas):
    #pide nombre para la cantidad de personas
    lista_personas = []
    for indice in range(cant_personas):
        lista_personas.append(solicitarValor("Ingrese nombre del jugador {0}".format(indice+1)))
    return lista_personas

def mostrarDatosJugador(jugador):
    print("datos jugador")

def mostrarDesaciertos(jugador):
    print("desaciertos jugador")

def mostrarAciertos(jugador):
    print("aciertos jugador")

