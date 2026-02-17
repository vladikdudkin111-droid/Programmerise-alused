"""Lisa kõikidesse sõnastikesse järgmised sõnad:

    headaega - goodbye - arrivederci
    pott - pot - pentola
    sõnastik - dictionary - dizionario

Tõlgi (väljastage ekraanile) järgmised sõnad:

    üks -> itaalia
    ciao - > eesti
    dog -> itaalia
    pentola - inglise """

import ülesanne3 as dicts

dicts.eesti_inglise_base["headaega"] = "goodbye"
dicts.eesti_inglise_base["pott"] = "pot"
dicts.eesti_inglise_base["sõnastik"] = "dictionary"

dicts.inglise_itaalia_base["goodbye"] = "arrivederci"
dicts.inglise_itaalia_base["pot"] = "pentola"
dicts.inglise_itaalia_base["dictionary"] = "dizionario"

dicts.eesti_itaalia_base["headaega"] = "arrivederci"
dicts.eesti_itaalia_base["pott"] = "pentola"
dicts.eesti_itaalia_base["sõnastik"] = "dizionario"

if __name__ == '__main__':
    print(f"üks -> itaalia: {dicts.eesti_itaalia_base['üks']}")
    print(f"ciao -> eesti: {dicts.itaalia_eesti_base['ciao']}")
    print(f"dog -> itaalia: {dicts.inglise_itaalia_base['dog']}")
    print(f"pentola -> inglise: {dicts.itaalia_inglise_base['pentola']}")





