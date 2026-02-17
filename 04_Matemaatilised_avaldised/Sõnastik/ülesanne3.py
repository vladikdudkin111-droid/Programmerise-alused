"""Loo juurde kaks uut sõnastiku (e_inglise, e_itaalia), mille võti ei ole mitte eesti keeles,
vaid vastavalt kas inglise või itaalia keeles. Lisa sõnastikku ka kõik eelmises sõnastikus olevad sõnad. """



def exchange_keys_and_values(exchange_dict: dict) -> dict:
    return {v: k for k, v in exchange_dict.items()}

if __name__ == "__main__":

    eesti_inglise_base = {
        "tere": "hello",
        "head aega": "goodbye",
        "raamat": "book",
        "õun": "apple"
    }

    eesti_itaalia_base = {
        "tere": "ciao",
        "head aega": "arrivederci",
        "raamat": "libro",
        "õun": "mela"
    }

    e_inglise = exchange_keys_and_values(eesti_inglise_base)
    e_itaalia = exchange_keys_and_values(eesti_itaalia_base)

    print("Inglise-Eesti:", e_inglise)
    print("Itaalia-Eesti:", e_itaalia)


def inglise_itaalia_base():
    return None


def itaalia_eesti_base():
    return None


def itaalia_inglise_base():
    return None