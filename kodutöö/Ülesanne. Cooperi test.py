def hinda(meetrid, sugu):
    if sugu == 'M':
        vaga_hea = 2800
        rahuldav = 2000
    else:  # N
        vaga_hea = 2600
        rahuldav = 1800

    if meetrid >= vaga_hea:
        return "väga hea"
    elif meetrid < rahuldav:
        puudu = rahuldav - meetrid
        return f"nõrk, järgmisest hindest puudu {puudu} m"
    else:
        puudu = vaga_hea - meetrid
        return f"rahuldav, järgmisest hindest puudu {puudu} m"


def keskmine_hinne(keskmine, sugu):
    """Leiame keskmise tulemuse hinde (kasutame sama hindamisfunktsiooni)."""
    return hinda(round(keskmine), sugu)


if __name__ == '__main__':
    failinimi = input("Sisesta failinimi: ")

    mehed = []
    naised = []

    with open(failinimi, encoding="utf-8") as f:
        for rida in f:
            meetrid, sugu = rida.split()
            meetrid = int(meetrid)

            hinne = hinda(meetrid, sugu)
            print(meetrid, sugu, "-", hinne)

            if sugu == 'M':
                mehed.append(meetrid)
            else:
                naised.append(meetrid)

    if mehed:
        keskm_m = round(sum(mehed) / len(mehed))
        print("Meeste keskmine:", keskm_m, "m")
        print("Meeste keskmine hinne:", keskmine_hinne(keskm_m, 'M'))

    if naised:
        keskm_n = round(sum(naised) / len(naised))
        print("Naiste keskmine:", keskm_n, "m")
        print("Naiste keskmine hinne:", keskmine_hinne(keskm_n, 'N'))