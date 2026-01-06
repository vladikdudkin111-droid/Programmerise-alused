"""Koosta mäng, kus saate ära arvata arvuti poolt mõeldud täisarvu ühest kahekümneni."""

from random import randint

def play_guessing_game():
    correct = randint(1, 20)
    while True:
        guess = int(input(">> "))

        if guess > correct:
            print("Liiga suur, provi uuesti.")
        elif guess < correct:
            print("Liiga väike, proovi uuesti.")
        else:
            print(f"Tubli, arvasid ära. Arv oli {correct}.")
        break

if __name__ == '__main__':
    play_guessing_game()