""" 1.       Küsi kasutaja nime
    2.       Kui nimepikkus on vahemikus 5 – 10 (kaasa arvatud), siis tervita 3 korda
    3.       Muidu küsi kolm arvu ja tagasta nende summa. (Kordus)"""

while True:
    nimi = input("Mis on sinu nimi? ")
    if 5 <= len(nimi) <= 10:
        for _ in range(3):
            print(f"Tere, {nimi}!")
    else:
        print("Nimi ei ole 5–10 tähemärki pikk.")
        arvud = []
        for i in range(1, 4):
            while True:
                try:
                    arv = float(input(f"Sisesta {i}. arv: "))
                    arvud.append(arv)
                    break
                except ValueError:
                    print("Palun kirjuta arv.")
        summa = sum(arvud)
        print(f"Arvude summa on: {summa}")
    print("\n--- Järgmine kordus ---\n")




