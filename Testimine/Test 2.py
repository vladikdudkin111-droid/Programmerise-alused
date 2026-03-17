"""Lahenda ülesanne (ära unusta docstringe)



Koosta programm telefoniraamatu loomiseks.



1.       Peab saama sisestada nime ja telefoni numbrit

2.       Samal nimel võib olla ainult üks telefoni number

3.       Peab saama küsida nime järgi numbrit ja numbri järgi nime

a.       Kui vastet pole, siis peab võimaldama lisamist

4.       Programmi sulgemine ei tohi andmeid kaotada (tuleb salvestada faili)

5.       Lisa funktsioon terve raamatu kuvamiseks"""

FILE = "phonebook.txt"


def load_data():
    """Loeb telefoniraamatu andmed failist ja tagastab sõnastiku."""
    phonebook = {}
    try:
        with open(FILE, "r", encoding="utf-8") as f:
            for line in f:
                name, number = line.strip().split(";")
                phonebook[name] = number
    except FileNotFoundError:
        pass
    return phonebook


def save_data(phonebook):
    """Salvestab telefoniraamatu andmed faili."""
    with open(FILE, "w", encoding="utf-8") as f:
        for name, number in phonebook.items():
            f.write(f"{name};{number}\n")


def add_contact(phonebook, name=None, number=None):
    """Lisab uue kontakti. Ühel nimel saab olla ainult üks number."""
    if name is None:
        name = input("Sisesta nimi: ")

    if name in phonebook:
        print("See nimi on juba olemas!")
        return

    if number is None:
        number = input("Sisesta number: ")

    phonebook[name] = number
    save_data(phonebook)
    print("Kontakt lisatud.")


def search_by_name(phonebook):
    """Otsib numbri nime järgi. Kui ei leia, pakub lisamist."""
    name = input("Sisesta nimi: ")

    if name in phonebook:
        print("Number:", phonebook[name])
    else:
        print("Kontakti ei leitud.")
        if input("Kas lisada uus kontakt? (j/e): ").lower() == "j":
            add_contact(phonebook, name=name)


def search_by_number(phonebook):
    """Otsib nime numbri järgi. Kui ei leia, pakub lisamist."""
    number = input("Sisesta number: ")

    for name, num in phonebook.items():
        if num == number:
            print("Nimi:", name)
            return

    print("Selle numbriga kontakti ei leitud.")
    if input("Kas lisada uus kontakt? (j/e): ").lower() == "j":
        add_contact(phonebook, number=number)


def show_all(phonebook):
    """Kuvab kogu telefoniraamatu."""
    if not phonebook:
        print("Telefoniraamat on tühi.")
        return

    print("\nTelefoniraamat:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")


def menu():
    """Kuvab menüü ja juhib programmi tööd."""
    phonebook = load_data()

    while True:
        print("\n1 - Lisa kontakt")
        print("2 - Otsi nime järgi")
        print("3 - Otsi numbri järgi")
        print("4 - Kuva kõik kontaktid")
        print("5 - Välju")

        choice = input("Valik: ")

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_by_name(phonebook)
        elif choice == "3":
            search_by_number(phonebook)
        elif choice == "4":
            show_all(phonebook)
        elif choice == "5":
            print("Programm lõpetatud.")
            break
        else:
            print("Vale valik!")


if __name__ == "__main__":
    menu()