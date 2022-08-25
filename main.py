import random
import sys


vidas = 5
Gameover = ""


def main(palavra):

    global Gameover
    print("\nVocê tem 5 tentativas para adivinhar qual é a palavra a seguir: ")
    print(embaralha(palavra))

    if Gameover == "Ganhou":
        sys.exit()
    elif Gameover == "Perdeu":
        sys.exit()
    else:
        while vidas > 0 and Gameover != "Perdeu" and Gameover != "Ganhou":
            acertarPalavra(palavra)


def acertarPalavra(palavra):

    tentativa = input("Palpite: ")

    if tentativa != palavra:
        global vidas
        vidas -= 1
        if vidas != 0:
            motivacional()
    elif tentativa == palavra:
        print("Parabéns! Você acertou.")
        global Gameover
        Gameover = "Ganhou"
        return

    if vidas == 0:
        Gameover = "Perdeu"
        print("\nVocê falhou! A palavra era: " + palavra)


def embaralha(palavraEmbaralhar):
    mistura = []
    for letra in palavraEmbaralhar:
        mistura.append(letra)
    random.shuffle(mistura)
    final = "".join(mistura)
    return final


def motivacional():
    frases = ["Você consegue!", "Não desista!", "Acredito em você!", "Falta pouco!"]
    motiv = frases[random.randint(0, 3)]
    print("\nVocê ainda tem " + f"{vidas}" + " tentativa(s)! " + motiv)


main("papagaio")
