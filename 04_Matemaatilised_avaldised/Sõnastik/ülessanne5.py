"""Morsetähestik on koodikomplekt, kus igale tekstisümbolile vastab pikkadest ja lühikestest signaalidest koosnev kood
(vt. https://et.wikipedia.org/wiki/Morse). Ilmselt on kõigile teada appikutse "SOS" kood: "... --- ..." ehk kolm
lühikest signaali ("S"), kolm pikka ("O") ja taas kolm lühikest. Lühikesi signaale tähistatakse punktide, pikki
aga kriipsudega.

Vajalik on sõnastik, kus on kirjas morse koodid (iga elemendi võtmeks tähistatav sümbol, väärtuseks koodi järjend
punktidest ja kriipsudest). Aja kokkuhoiu mõttes võid kasutada sellist rida:
tahestik = {"a":".-", "b":"-...", "c":"-.-.", "d":"-..", "e":".", "f":"..-.", "g":"--.", "h":"....", "i":"..",
"j":".---", "k":"-.-", "l":".-..", "m":"--", "n":"-.", "o":"---", "p":".--.", "q":"--.-", "r":".-.", "s":"...",
"t":"-", "u":"..-", "v":"...-", "w":".--", "x":"-..-", "y":"-.--", "z":"--.."}

Koosta programm, mis programmi käivitamisel tervitab kasutajat nii tavakeeles kui morse koodina, lubab seejärel
kasutajal sisestada sõnu ning teisendab need sümbolhaaval morsetähestikku (lisades iga sümboli järele tühiku).
Sõnastik ei pruugi sisaldada kõikvõimalikke märke, seega tuleb iga sümboli puhul kontrollida, kas see üldse esineb
sõnastikus. Tähe registrit ehk suur- ja väiketähti ei eristata. Samuti tuleb otsustada, mida ette võtta nende
tähtedega, mida inglise tähestikus pole (näiteks "õ", "ä" jne): ignoreerida või mõned neist teisendada
(näiteks "õ" -> "o" vms).

Programm võiks küsida kasutajalt sõnu kas mingi arv kordi või töötada lõpmatult, kuni kasutaja
sõna ei sisesta, vaid vajutab lihtsalt sisestusklahvile. """


def morse_translator():
    tahestik = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.",
        "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..",
        "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
        "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-",
        "y": "-.--", "z": "--.."
    }


    def translate_to_morse(text):
        replacements = {'õ': 'o', 'ä': 'a', 'ö': 'o', 'ü': 'u'}
        processed_text = text.lower()
        for char, rep in replacements.items():
            processed_text = processed_text.replace(char, rep)
        result = []
        for char in processed_text:
            if char in tahestik:
                result.append(tahestik[char])
            elif char == " ":
                result.append(" ")
        return " ".join(result)


    welcome_text = "tere"
    print(f"{welcome_text.capitalize()}! / {translate_to_morse(welcome_text)}")
    print("Sisesta sõna (või vajuta Enter lõpetamiseks):")

    while True:
        user_input = input("> ")
        if not user_input.strip():
            print("Head aega!")
            break
        morse_output = translate_to_morse(user_input)
        if morse_output.strip():
            print(f"Morse: {morse_output}")
        else:
            print("Selles sõnas polnud sümboleid, mida saaks morsesse tõlkida.")


if __name__ == "__main__":
    morse_translator()
