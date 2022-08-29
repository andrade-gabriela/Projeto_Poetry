import random
import sys

vidas = 5
Gameover = ""


def main():

    dificuldade = input("Digite o número correspondente a dificuldade desejada: \n 1- Fácil \n 2- Médio \n 3- Difícil \n")
    tema = input("\n Digite o número correspondente ao tema desejado: \n 1- Alimentos \n 2- Animais \n 3- Cidade \n 4- Marcas \n 5- Objetos \n 6- Países \n")

    palavra = (temas(dificuldade,tema)).lower()
    

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

def temas(nivel,tema):
    alimentos = ["Alface","Bolacha","Chocolate","Dobradinha","Espaguete","Farofa","Gelatina","Hamburguer","Iogurte","Jaca","Kiwi","Leite","Mandioca","Nachos","Ovo","Patê","Queijo","Rúcula","Sorvete","Tangerina","Uva","Vatapá","Yakisoba"]
    animais = ["Anta","Andorinha","Bode","Camelo","Cachorro","Dromedário","Dinossauro","Escorpião","Foca","Formiga","Gato","Girafa","Hipopótamo","Iguana","Jabuti","Leão","Lagartixa","Morcego","Ovelha","Pato","Pernilongo","Quati","Tamanduá","Urso","Vespa"]
    cidades = ["Adamantina","Aracaju","Antas","Bagé","Bandeirantes","Barueri","Chapecó","Canavieiras","Curitiba","Diamantina","Exu","Florianópolis","Franca","Goiânia","Itajaí","Itu","Natal","Palmas","Recife","Sorocaba","Teresina","Umuarama","Varginha"]
    marcas = ["Antartica","Adidas","Apple","Bic","Balenciaga","Chanel","Colgate","Corona","Disney","Electrolux","Ford","Gillette","Google","Gucci","Intel","Jeep","Kalunga","Lacoste","Motorola","Microsoft","Nike","Outback","Panasonic","Renault","Sony","Universal","Vans"]
    objetos = ["Agulha","Alfinete","Bola","Borracha","Copo","Caneta","Dado","Dedal","Escova","Esmalte","Espelho","Faca","Fornalha","Gaiola","Garfo","Holoforte","Imã","Isqueiro","Jarra","Luva","Lapiseira","Maquiagem","Navalha","Óculos","Pedra","Quadro","Régua","Urna","Ventilador","Vassoura","Xícara","Zíper"]
    paises = ["Alemanha","Angola","Argentina","Brasil","Bélgica","Canadá","Catar","Chile","China","Colômbia","Dinamarca","Egito","Eslováquia","Guatemala","Haiti","Iraque","Madagascar","Moçambique","Panamá","Paquistão","Peru","Portugal","Rússia","Tailândia","Ucrânia","Vaticano","Zâmbia"]

    if tema == "1":
        return random.choice(filtra_dificuldade(nivel,alimentos))
    elif tema == "2":
        return random.choice(filtra_dificuldade(nivel,animais))
    elif tema == "3":
        return random.choice(filtra_dificuldade(nivel,cidades))
    elif tema == "4":
        return random.choice(filtra_dificuldade(nivel,marcas))
    elif tema == "5":
        return random.choice(filtra_dificuldade(nivel,objetos))
    elif tema == "6":
        return random.choice(filtra_dificuldade(nivel,paises))
    else:
        return "\nNúmero inválido! Por favor, insira um número de 1 a 6\n"

def filtra_dificuldade(nivel, lista):

    if nivel == "1":

        filtro = [elemento for elemento in lista if len(elemento) <= 4]  
        return filtro

    if nivel == "2":

        filtro = [elemento for elemento in lista if len(elemento) > 5 and len(elemento) < 7]  
        return filtro
        
    if nivel == "3":

        filtro = [elemento for elemento in lista if len(elemento) >= 7]  
        return filtro

 

main()

