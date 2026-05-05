from maja import Maja
from eramaja import Eramaja


def naita_hinda(maja):
    """Kuva hind."""
    print(f"Hind: {maja.hinda()} €")


if __name__ == "__main__":
    print("Test:\n")

    test_maja = Maja(3, 2, "Testi 1")
    test_eramaja = Eramaja(5, 2, "Testi 2", 700)

    test_maja.prindi_andmed()
    print("Kirjeldus:", test_maja.kirjeldus())
    naita_hinda(test_maja)

    test_maja.renoveeri(4)
    print("\nPärast renoveerimist:")
    test_maja.prindi_andmed()

    print()

    test_eramaja.prindi_andmed()
    naita_hinda(test_eramaja)

    test_eramaja.suurenda_aeda(100)
    print("\nPärast muutust:")
    test_eramaja.prindi_andmed()

    print("\nJärjend:\n")

    majad = []

    for i in range(60):
        majad.append(Maja(2 + (i % 5), 1 + (i % 3), f"Maja {i+1}"))

    for i in range(40):
        majad.append(Eramaja(3 + (i % 4), 1 + (i % 2), f"Eramaja {i+1}", 400 + i * 10))

    # Polümorfism
    for maja in majad[:5]:
        maja.prindi_andmed()
        naita_hinda(maja)
        print()

    koguhind = sum(maja.hinda() for maja in majad)

    print(f"Koguhind: {koguhind} €")
    print(f"Kokku maju: {Maja.maja_arv}")