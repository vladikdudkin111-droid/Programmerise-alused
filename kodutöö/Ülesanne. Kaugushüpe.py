def tegelik_tulemus(vigane, parandus_cm):
    """
    Arvutab tegeliku kaugushüppe tulemuse meetrites.

    Args:
        vigane (float): vigane tulemus meetrites
        parandus_cm (float): paranduse suurus sentimeetrites

    Returns:
        float: tegelik tulemus meetrites
    """
    return vigane + parandus_cm / 100


if __name__ == '__main__':
    failinimi = input("Sisesta failinimi: ")

    try:
        with open(failinimi, encoding="utf-8") as f:
            vigased = [float(rida.strip()) for rida in f if rida.strip()]
    except FileNotFoundError:
        print("Faili ei leitud. Kontrolli failinime ja asukohta.")
        exit()

    parandus_cm = float(input("Sisesta mõõteparandus (cm): "))
    normatiiv = float(input("Sisesta meistrivõistluste normatiiv (m): "))

    tegelikud = [tegelik_tulemus(v, parandus_cm) for v in vigased]

    print("\nTegeliku tulemused:")
    for t in tegelikud:
        print(f"{t:.2f} m")

    # normatiivi täitjate arv ja keskmine
    normi_taitjad = [t for t in tegelikud if t >= normatiiv]

    print(f"\nNormatiivi täitjate arv: {len(normi_taitjad)}")
    if normi_taitjad:
        keskmine = sum(normi_taitjad) / len(normi_taitjad)
        print(f"Normatiivi täitjate keskmine: {keskmine:.2f} m")