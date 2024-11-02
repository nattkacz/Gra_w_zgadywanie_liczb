# Gra_w_zgadywanie_liczb

Prosta gra konsolowa w Pythonie, w której gracz próbuje odgadnąć losowo wygenerowaną liczbę z zakresu od 1 do 100. Gra dostarcza informacji zwrotnej po każdej próbie, wskazując, czy podana liczba jest za wysoka, za niska, czy poprawna. Gra trwa, aż gracz zgadnie prawidłową liczbę.

## Funkcjonalności

- **Generowanie Losowej Liczby**: Każda gra rozpoczyna się od wygenerowania nowej liczby w zakresie od 1 do 100.
- **Informacje Zwrotne dla Gracza**: Gra informuje, czy zgadywana liczba jest za wysoka lub za niska, pomagając graczowi w znalezieniu prawidłowej odpowiedzi.
- **Obsługa Błędów**: Gra radzi sobie z błędnymi danymi wejściowymi (np. tekstem zamiast liczby) i prosi gracza o podanie prawidłowej liczby.

## Jak Zacząć

### Wymagania

- Python 3.x

### Instalacja

1. Sklonuj repozytorium:
   '''git clone https://github.com/twojanazwauzytkownika/Gra_w_zgadywanie_liczb.git
2. Przejdź do katalogu z projektem:
   '''cd Gra_w_zgadywanie_liczb

### Użycie

Uruchom program za pomocą Pythona w terminalu:
'''python guess.py

Gra poprosi o wpisanie liczby z zakresu od 1 do 100. Na podstawie podanego numeru gra poinformuje, czy jest on „Za wysoki” czy „Za niski”, aż gracz zgadnie prawidłową liczbę.

## Przegląd Kodu
Gra składa się z dwóch głównych funkcji:

##get_number(): Obsługuje dane wejściowe użytkownika, sprawdzając, czy wpisana wartość jest liczbą całkowitą w wymaganym zakresie.
##guess_number(): Główna pętla gry, która generuje losową liczbę docelową, porównuje ją z liczbami podanymi przez użytkownika i dostarcza informacji zwrotnej do momentu, aż gracz wygra.

## Przykład
Zgadnij liczbę między 1 a 100: 50  
Za niska
Zgadnij liczbę między 1 a 100: 75  
Za wysoka
Zgadnij liczbę między 1 a 100: 63  
Udało się, zgadłeś liczbę!

