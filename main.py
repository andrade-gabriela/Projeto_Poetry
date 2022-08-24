import random
def main(palavra):
    compara = embaralha(palavra)

    print("Você tem 5 tentativas para adivinhar qual é a palavra a seguir: "+compara)
    tentativa = ""
    for i in range(5):
        if tentativa != palavra:
            if i < 4:
                tentativa = input("Tentativa "+ f"{i+1}" +": ")
                print("Você ainda tem "+ f"{4-i}" +" tentativas! " + motivacional())
            else:
                tentativa = input("Tentativa "+ f"{i+1}" +": ")
                print("Você ainda tem "+ f"{4-i}" +" tentativa! " + motivacional())
        else:
            print("Parabéns! Você acertou.")

    print("Você falhou! A palavra era: " + palavra)

def embaralha(p):
    mistura = []
    for letra in p:
        mistura.append(letra)
    mistura.sort()
    final = "".join(mistura)
    return final

def motivacional():
    frases = ["Você consegue!",
            "Não desista!",
            "Acredito em você!",
            "Falta pouco!"]
    return frases[random.randint(0,3)]


main("papagaio")
