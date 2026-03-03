"""Koosta programm, mis küsib kasutajalt rea, mille järele ta soovib failis luuletus.txt
uut rida lisada ning seejärel lisab kasutaja poolt sisestatud rea nt:
Sisesta rida, mille järele soovid uut rida lisada:
>> Padja, teki viskan maha,
Sisesta rida, mida soovid lisada:
>> üles ärgata ma ei taha,

Tulemus failis luuletus.txt:
Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
üles ärgata ma ei taha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin."""


def lisa_rida_faili(failinimi, otsitav_rida, lisatav_rida):
    """Otsib failist rida ja lisab selle järel uue teksti."""
    try:
        with open(failinimi, "r", encoding="utf-8") as f:
            read = f.readlines()

        leitud = False
        for i in range(len(read)):
            if read[i].strip() == otsitav_rida.strip():
                # Lisame uue rea (koos reavahetusega) leitud rea järel olevasse indeksisse
                read.insert(i + 1, lisatav_rida.strip() + "\n")
                leitud = True
                break  # Peatume esimese vaste leidmisel

        if leitud:
            with open(failinimi, "w", encoding="utf-8") as f:
                f.writelines(read)
            print("\nFaili uuendamine õnnestus!")
        else:
            print("\nViga: Sellist rida ei leitud failist.")

    except FileNotFoundError:
        print("Viga: Faili ei leitud.")


def main():
    fail = "luuletus.txt"

    otsitav = input("Sisesta rida, mille järele soovid uut rida lisada:\n>> ")
    lisatav = input("Sisesta rida, mida soovid lisada:\n>> ")

    lisa_rida_faili(fail, otsitav, lisatav)


if __name__ == "__main__":
   main()
