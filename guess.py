import random

'''
   Program do zgadywania liczby.
   Użytkownik próbuje odgadnąć losowo wygenerowaną liczbę między 1 a 100,
   otrzymując informacje zwrotne, czy podana liczba jest za wysoka czy za niska.
'''
def get_number():
    """
          Prosi użytkownika o zgadnięcie liczby między 1 a 100 i zwraca poprawne dane wejściowe.

          Returns:
              int: Poprawna liczba wprowadzona przez użytkownika.
    """
    while True:
        try:
            result = int(input("Guess a number between 1 and 100: "))
            break
        except ValueError:
            print("Please enter a number")
    return result



def guess_number():
    """
       Główna funkcja generująca losową liczbę i porównująca ją z odgadniętą przez użytkownika.

       Funkcja kontynuuje prośby o zgadywanie, dopóki użytkownik nie odgadnie poprawnie,
       dostarczając informacje zwrotne, czy zgadnięta liczba jest za wysoka czy za niska.
    """
    number = int(random.randint(1,101))
    guess = get_number()
    while guess != number:
        if guess > number:
            print("Too high")
        elif guess < number:
            print("Too low")
        guess = get_number()
    print("You guessed the number!")




if __name__ == '__main__':
    guess_number()
   

