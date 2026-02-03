"""Koosta programm, mis "viskab täringut" kolm korda ehk väljastab ekraanile 3 juhusliku täringuviske tulemused.
Et ekraanipilt oleks realistlikum, esita tulemused graafiliselt, selleks kasuta nn. ASCII graafikat
(https://en.wikipedia.org/wiki/ASCII_art): imiteeri tekstisümbolite abil täringu külje kujutist. Täiendamiseks:

    Kasutaja võib alguses ise valida, mitu korda täringut visata.
    Mängida võib mitu inimest, programmi alguses küsitakse inimeste nimesid.
    Täringut imiteeritakse kolmemõõtmelisena. """

import random

DICE_3D = {
    1: [
        " _____",
        "|     |",
        "|  •  |",
        "|_____|"
    ],
    2: [

        " _____",
        "|  •  |",
        "|   • |",
        "|_____|"
    ],
    3: [
        " _____",
        "|  •  |",
        "| • • |",
        "|_____|"
    ],
    4: [
        " _____",
        "| • • |",
        "| • • |",
        "|_____|"
    ],
    5: [
        " _____",
        "| • • |",
        "| ••• |",
        "|_____|"
    ],
    6: [
        " _____",
        "| ••• |",
        "| ••• |",
        "|_____|"
    ],
}

def print_dice(value):
    for line in DICE_3D[value]:
        print(line)

players = input("Sisesta mängijate nimed (komadega eraldatult): ").split(",")
players = [p.strip() for p in players]

throws = int(input("Mitu korda täringut visatakse?: "))

print("\n MÄNG ALGAB \n")

for player in players:
    print(f"\nMängija: {player}")
    for i in range(throws):
        roll = random.randint(1, 6)
        print(f"\nVise {i + 1}: ({roll})")
        print_dice(roll)

if __name__ == '__main__':
    print_dice()