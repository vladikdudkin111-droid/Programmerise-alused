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
    """Loeb telefoniraamatu andmed failist."""
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
            f.write(name + ";" + number + "\n")


def add_contact(phonebook, name=None, number=None):
    """Lisab uue kontakti telefoniraamatusse."""
    if name is None:
        name = input("Name: ")

    if name in phonebook:
        print("This name already exists.")
        return

    if number is None:
        number = input("Number: ")

    phonebook[name] = number
    save_data(phonebook)
    print("Contact added.")


def search_by_name(phonebook):
    """Otsib numbri nime järgi."""
    name = input("Enter name: ")

    if name in phonebook:
        print("Number:", phonebook[name])
    else:
        print("Contact not found.")
        choice = input("Add new contact? (y/n): ")
        if choice.lower() == "y":
            add_contact(phonebook, name)

    print("Number not found.")
    choice = input("Add new contact? (y/n): ")
    if choice.lower() == "y":
        name = input("Enter name: ")
        add_contact(phonebook, name, number)


def show_all(phonebook):
    """Kuvab kogu telefoniraamatu."""
    if not phonebook:
        print("Phonebook is empty.")
        return

    for name, number in phonebook.items():
        print(name, number)


def menu():
    """Programmi menüü."""
    phonebook = load_data()

    while True:
        print("\n1 - Add contact")
        print("2 - Search by name")
        print("3 - Search by number")
        print("4 - Show all contacts")
        print("5 - Exit")

        choice = input("Choice: ")

        if choice == "1":
            add_contact(phonebook)
        elif choice == "2":
            search_by_name(phonebook)
        elif choice == "3":
            search_by_number(phonebook)
        elif choice == "4":
            show_all(phonebook)
        elif choice == "5":
            break
        else:
            print("Wrong choice")


if __name__ == "__main__":
    menu()