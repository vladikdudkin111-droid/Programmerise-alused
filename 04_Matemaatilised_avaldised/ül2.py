"""Tee uus fail luuletus.txt ning lisa sinna järgmine luuletus:
Hommikul kui üles ärkan,
arvutit ma laual märkan.
Padja, teki viskan maha,
jooksen ruttu compu taha.
Kiirelt sisestan parooli,
kuid juba tuleb minna kooli.
Error tuleb ette siis,
kool on mulle räme piin.

Koosta programm, mis kuvab ekraanile luuletuse read, kuid lisab nende ette rea
järjekorranumbri ja iga rea järele sulgudesse reas asuvate sümbolite arvu e. rea pikkuse. """

def creat_file(filename: str):
    failinimi = "luuletus.txt"
    sisu = [
        "Hommikul kui üles ärkan,",
        "arvutit ma laual märkan.",
        "Padja, teki viskan maha,",
        "jooksen ruttu compu taha.",
        "Kiirelt sisestan parooli,",
        "kuid juba tuleb minna kooli.",
        "Error tuleb ette siis,",
        "kool on mulle räme piin."
    ]

    # Loome faili ja kirjutame luuletuse sisse
    with open(failinimi, "w", encoding="utf-8") as f:
        for rida in sisu:
            f.write(rida + "\n")

    # Loeme failist ja kuvame soovitud kujul
    print("Faili töötlemise tulemus:\n")
    with open(failinimi, "r", encoding="utf-8") as f:
        for i, rida in enumerate(f, start=1):
            puhas_rida = rida.strip()
            pikkus = len(puhas_rida)
            print(f"{i}. {puhas_rida} ({pikkus})")




if __name__ == "__main__":
    filename = "luuletus.txt"
    creat_file(filename)
