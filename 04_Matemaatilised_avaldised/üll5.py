"""Palindroomiks nimetatakse sõna (ka sõnaühendit), mis on nii vasakult paremale kui paremalt vasakule lugedes täpselt
 ühesugunem (näit. "kook", "kuulilennuteetunneliluuk" jne). Loo programm, mis trükib ekraanile välja kõik tekstifailis
  olevad sõnad, mis on palindroomid. Alustekstiks võid kasutada suvalist teksti, kuid katsetada tasuks ka sõnaloenditega,
kus iga sõna asub eraldi real (näit. eesti keele sõnade algvormid e. lemmad veebilehelt
 http://www.eki.ee/tarkvara/wordlist/). """


def lisa_rida_teksti_vahele(failinimi, otsitav, uus_rida):
    """Leiab rea ja lisab selle järel uue teksti."""
    try:
        # Loeme faili sisu listi
        with open(failinimi, "r", encoding="utf-8") as f:
            read = f.readlines()

        leitud = False
        uus_sisu = []

        for rida in read:
            uus_sisu.append(rida)
            # Kui leiame otsitava rea, lisame kohe selle järel uue rea
            if rida.strip() == otsitav.strip():
                uus_sisu.append(uus_rida.strip() + "\n")
                leitud = True

        if leitud:
            # Kirjutame muudetud sisu faili tagasi
            with open(failinimi, "w", encoding="utf-8") as f:
                f.writelines(uus_sisu)
            print("\nFail on edukalt uuendatud!")
        else:
            print("\nViga: Sellist rida ei leitud failist.")

    except FileNotFoundError:
        print("Viga: Faili ei leitud!")


def main():
    failinimi = "luuletus.txt"

    otsitav = input("Sisesta rida, mille järele soovid uut rida lisada:\n>> ")
    lisatav = input("Sisesta rida, mida soovid lisada:\n>> ")

    lisa_rida_teksti_vahele(failinimi, otsitav, lisatav)


if __name__ == "__main__":
    main()
