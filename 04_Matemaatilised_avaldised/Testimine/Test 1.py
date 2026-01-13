""" 1.       Küsi kasutaja nime
    2.       Kui nimepikkus on vahemikus 5 – 10 (kaasa arvatud), siis tervita 3 korda
    3.       Muidu küsi kolm arvu ja tagasta nende summa. (Kordus)"""


def tervita_nimega():
    nimi = input("Mis on sinu nimi? ")
    pikkus = len(nimi)
    if 5 <= pikkus <= 10:
        for _ in range(3):
            print(f"Tere, {nimi}!")
    else:
        summa = arvude_summa()
        print(f"Kolme arvu summa on: {summa}")


def arvude_summa():
    summa = 0
    for i in range(3):
        arv = int(input(f"Sisesta {i + 1}. arv: "))
        summa += arv
    return summa


def main():
    tervita_nimega()


if __name__ == "__main__":
    main()