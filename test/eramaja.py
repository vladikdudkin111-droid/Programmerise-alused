from maja import Maja


class Eramaja(Maja):
    """Eramaja klass."""

    def __init__(self, tubade_arv, korrused, aadress, aia_suurus=500):
        """Loo eramaja."""
        super().__init__(tubade_arv, korrused, aadress)
        self.aia_suurus = aia_suurus

    def prindi_andmed(self):
        """Kuva eramaja andmed."""
        print("Eramaja:")
        print(self)
        print(f"Aia suurus: {self.aia_suurus} m²")

    def hinda(self):
        """Tagasta eramaja hind."""
        return super().hinda() + self.aia_suurus * 100

    def suurenda_aeda(self, suurus):
        """Suurenda aeda."""
        self.aia_suurus += suurus