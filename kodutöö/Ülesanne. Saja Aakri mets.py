def aastane_juurkasu(aakrid, juurdekasv_tm_ha):
    """
    Arvutab metsatüki aastase juurdekasvu tihumeetrites.

    Args:
        aakrid (float): metsatüki pindala aakrites
        juurdekasv_tm_ha (float): aastane juurdekasv hektari kohta tm/ha

    Returns:
        float: metsatüki aastane juurdekasv tm, ümardatuna sajandikeni
    """
    # 1 aaker = 0,4047 hektarit
    hektarid = aakrid * 0.4047
    juurdekasv = hektarid * juurdekasv_tm_ha
    return round(juurdekasv, 2)


if __name__ == '__main__':
    failinimi = input("Sisesta failinimi: ")

    try:
        with open(failinimi, encoding="utf-8") as f:
            pindalad = [float(rida.strip()) for rida in f if rida.strip()]
    except FileNotFoundError:
        print("Faili ei leitud. Kontrolli failinime ja asukohta.")
        exit()

    juurdekasv_tm_ha = float(input("Sisesta puuliigi aastane juurdekasv (tm/ha): "))
    piir_aakrites = float(input("Sisesta piirväärtus aakrites: "))

    loetud_tukid = 0

    for pindala in pindalad:
        if pindala > piir_aakrites:
            kasv = aastane_juurkasu(pindala, juurdekasv_tm_ha)
            print(f"Metsatüki pindala: {pindala} aakrit, aastane juurdekasv: {kasv} tm")
            loetud_tukid += 1
        else:
            print(f"Metsatükki ei võeta arvesse (pindala: {pindala} aakrit)")

    print(f"\nAastane juurdekasv arvutati {loetud_tukid} metsatükile.")