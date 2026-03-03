"""Tee programm, mis väljastab failist luuletus.txt kasutaja poolt soovitud rea nt:
Mitmendat rida soovid kuvada:
>> 7
Error tuleb ette siis,

NB! Faili avamiseks ja rea väljastamiseks koosta eraldi alamprogramm (ehk funktsioon). """


def loe_rida_failist(failinimi, rea_number):
    """Avab faili ja tagastab soovitud järjekorranumbriga rea."""
    try:
        with open(failinimi, "r", encoding="utf-8") as f:
            read = f.readlines()
            # Kontrollime, kas soovitud rida on failis olemas
            if 1 <= rea_number <= len(read):
                return read[rea_number - 1].strip()
            else:
                return "Viga: Sellise numbriga rida failis ei ole."
    except FileNotFoundError:
        return "Viga: Faili 'luuletus.txt' ei leitud. Käivita esmalt esimene programm."


def main():
    failinimi = "luuletus.txt"

    try:
        valik = int(input("Mitmendat rida soovid kuvada:\n>> "))
        tulemus = loe_rida_failist(failinimi, valik)
        print(tulemus)
    except ValueError:
        print("Viga: Palun sisesta täisarv.")


if __name__ == "__main__":
    filename = "luuletus.txt"
