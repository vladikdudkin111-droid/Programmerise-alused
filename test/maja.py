"""Klassi Harjutus

Loo klass maja andmete hoidmiseks (tubade arv, korrused, aadress)
Lisa käsklus maja andmete väljatrükiks
Lisa käsklus maja renoveerimiseks (muuda tubade arvu)
Lisa käsklus maja hindamiseks

Loo majast pärinev klass, demonstreeri polümorfismi toimimist."""

class Maja:
    """Üldine maja klass."""

    maja_arv = 0

    def __init__(self, tubade_arv, korrused, aadress):
        """Loo uus maja."""
        self.tubade_arv = tubade_arv
        self.korrused = korrused
        self.aadress = aadress
        self.seisukord = 0.8 + (tubade_arv * 0.05)

        Maja.maja_arv += 1

    def prindi_andmed(self):
        """Kuva andmed."""
        print(self)

    def kirjeldus(self):
        """Tagasta kirjeldus."""
        return f"{self.tubade_arv} tuba, {self.korrused} korrust"

    def renoveeri(self, uus_tubade_arv):
        """Muuda tubade arvu."""
        self.tubade_arv = uus_tubade_arv
        self.seisukord = min(self.seisukord + 0.1, 1.2)

    def hinda(self):
        """Tagasta hind."""
        hind = self.tubade_arv * 20000 + self.korrused * 50000
        return int(hind * self.seisukord)

    def __str__(self):
        """Tekstiline esitus."""
        return (f"Aadress: {self.aadress}\n"
                f"Tubade arv: {self.tubade_arv}\n"
                f"Korrused: {self.korrused}\n"
                f"Seisukord: {round(self.seisukord, 2)}")
