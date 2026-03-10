def loomade_lopupikkus(lopp_pikkus, loimede_arv):
    """
    Arvutab vaiba lõimede kogupikkuse meetrites, ümardatuna sajandikeni.

    Args:
        lopp_pikkus (float): vaiba lõpp-pikkus meetrites
        loimede_arv (int): lõimede arv

    Returns:
        float: lõimede kogupikkus meetrites, ümardatuna sajandikeni
    """
    # Algpikkus võetakse 20% suuremana, lisatakse kummalegi otsale 0.25 m
    algpikkus = lopp_pikkus * 1.2
    kogupikkus = loimede_arv * (algpikkus + 0.25 * 2)
    return round(kogupikkus, 2)


if __name__ == '__main__':
    failinimi = input("Sisesta failinimi: ")

    try:
        with open(failinimi, encoding="utf-8") as f:
            vaibad = [float(rida.strip()) for rida in f if rida.strip()]
    except FileNotFoundError:
        print("Faili ei leitud. Kontrolli failinime ja asukohta.")
        exit()

    kogusumma = 0.0

    for vpikkus in vaibad:
        # lõimede arv: 5-meetrised ja pikemad = 10, lühemad = 8 (näiteks)
        loimede_arv = 10 if vpikkus >= 5 else 8
        kogupikkus = loomade_lopupikkus(vpikkus, loimede_arv)
        print(f"Vaiba lõpp-pikkus: {vpikkus} m, lõimede arv: {loimede_arv}, kogupikkus: {kogupikkus} m")
        kogusumma += kogupikkus

    print(f"Kõigi vaipade lõimede kogupikkus kokku: {round(kogusumma, 2)} m")