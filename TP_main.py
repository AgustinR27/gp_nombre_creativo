from TP_texto import obtener_texto
import random

def formatear_palabras(palabra):
    dic_a_reemplazar = {"Ñ": "NI", "Á": "A", "É": "E", "Í": "I", "Ó": "O", "Ú": "U"}
    palabra_vieja = palabra.upper()
    palabra_nueva = ''
    for letra in palabra_vieja:
        if letra not in dic_a_reemplazar:
            palabra_nueva += letra
        else:
            palabra_nueva += dic_a_reemplazar[letra]
    return palabra_nueva


def obtener_palabras():
    texto = obtener_texto()
    dic_palabras = {}
    for linea in texto:
        if len(linea) > 0:
            lista_aux = linea.split(" ")
            for palabra in lista_aux:
                if palabra.isalpha() and len(palabra) >= 5:
                    if formatear_palabras(palabra) not in dic_palabras:
                        dic_palabras[formatear_palabras(palabra)] = 1
                    else:
                        dic_palabras[formatear_palabras(palabra)] += 1
    return dic_palabras


def enlistar_palabras(dic_palabras):
    lista_palabras = []
    for clave in dic_palabras:
        if clave not in lista_palabras:
            lista_palabras.append(clave)
    return lista_palabras


def palabra_adivinar(lista_palabras):
    palabra_adivinar = random.choice(lista_palabras)
    return palabra_adivinar
