"""Loo fail "astendamine.py", mis sisaldab funktsioone ruut(arv), kuup(arv), astenda(arv, aste).
Funktsioonid tagastavad vastavalt arvu ruudu, kuubi või arvu vastavas astmes. Faili "astendamine.py"
hakkame nüüd kasutama moodulina.

Koosta lisaks programm "kalkulaator.py", mis küsib kasutajalt arvu, mida ta soovib tõsta ruutu, kuupi või
 mingisse teise astmesse ning väljastab vastavalt kasutaja soovile vastuse. Programm peaks oma töös kasutama
 faili "astendamine.py", selleks kirjuta programmi algusesse rida "import astendamine", niimoodi saab programm
 "kalkulaator.py" kasutada kõiki programmis "astendamine.py" olevaid funktsioone. """

def create_familiars_file():
    familiars = [
        "Tiit Sukk"
        "Teet Pukk"
        "Peep Nukk"
        "Tina Kukk"
        "Mari Tukk"
        "Sari Lukk"
    ]
    with open("tuttavad.txt", "w", encoding="utf-8") as f:
        for name in familiars:
            f.write(name + "\n")

def read_names_from(filename: str) -> list[str]:
    result = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            if len(line) > 0:
                result.append(line.strip())
    return result

def sort_names(names, names_dict=None):
    for name in names:
        # võta nimest välja perekonna nimi (viimane)
        last_name = name.split()[-1]
        names_dict[(last_name, name)] = name

        #sorteeri
        sorted_keys = sorted(list(names_dict.keys()))
        print(sorted_keys)

        #tagasta
        return [item[-1] for item in sorted_keys]

if __name__ == "__main__":
    filename = "tuttavad.txt"
    create_familiars_file(filename)
    names_from_file = read_names_from(filename)
    sorted_by_last_name = sort_names(names_from_file)
    for name in sorted_by_last_name:
        print(name)