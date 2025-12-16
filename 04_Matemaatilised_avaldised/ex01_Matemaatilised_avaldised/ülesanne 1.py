"""Koosta programm, mis küsib kasutajalt ristküliku lähiskülgede pikkused ning väljastab ekraanile
 ristküliku ümbermõõdu ja pindala."""

def compute_rectangle():
    lenght = float(input("sisesta ristküliku pikkus"))
    width = float(input("sisesta ristküliku laius"))
    area = width * lenght
    circumference = 2 * (lenght + width)
    print(f"Antud ristküliku pindala on {area}")
    print(f"ümbermõõt on {circumference}")

    if __name__ == "__main__":
        compute_rectangle()