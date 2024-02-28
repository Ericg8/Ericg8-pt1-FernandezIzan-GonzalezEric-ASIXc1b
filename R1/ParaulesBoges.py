"""
Eric González, Izan Fernandez
28/02/2024
M03 UF2
Descripció: Pt1 Disseny Modular: ParaulesBoges
"""
import random
import string
#Obtiene una frase del usuario.
def obtener_frase_usuario():

    frase = input("Introduce una frase: ")
    return frase

#Desordena las letras de una palabra, excepto la primera y la última.
def desordenar_palabra(palabra):
    if len(palabra) > 3:
        primer_caracter = palabra[0]
        ultimo_caracter = palabra[-1]
        letras_intermedias = list(palabra[1:-1])
        random.shuffle(letras_intermedias)
        palabra_desordenada = primer_caracter + "".join(letras_intermedias) + ultimo_caracter
        return palabra_desordenada
    else:
        return palabra

#Procesa la frase desordenando las palabras.
def procesar_frase(frase):

    palabras = frase.split(" ")
    for i in range(len(palabras)):
        palabra = palabras[i]
        # Verificar si la palabra tiene signos de puntuación al final
        signos_puntuacion = string.punctuation
        ultimo_caracter = palabra[-1]
        if ultimo_caracter in signos_puntuacion:
            palabra_sin_puntuacion = palabra[:-1]
            palabra_desordenada = desordenar_palabra(palabra_sin_puntuacion) + ultimo_caracter
        else:
            palabra_desordenada = desordenar_palabra(palabra)
        palabras[i] = palabra_desordenada
    return " ".join(palabras)

#Función principal que ejecuta el programa:
def main():

    frase_usuario = obtener_frase_usuario()
    frase_procesada = procesar_frase(frase_usuario)
    print(frase_procesada)

# Llamada a la función principal
if __name__ == "__main__":
    main()

