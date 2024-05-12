def wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna):
    koszt = 0 # wpisz koszt
    
    # Koszty podstawowe
    if odleglosc == 'lokalna':
        koszt += 2
    elif odleglosc == 'krajowa':
        koszt += 12
    elif odleglosc == 'dalekobiezna':
        koszt += 20
    
    if typ == 'list':
        koszt += 7
    elif typ == 'paczka':
        koszt += 0  # paczka nie ma dodatkowych opłat
    
    # Potwierdzenie odbioru
    if potwierdzenie_odbioru:
        koszt += 7
    
    # Opcje specjalne
    if specjalna == 'wyjec':
        koszt += 4
    elif specjalna == 'list_gonczy':
        koszt += 12  # 1 sykl + 2 knuty
    
    # Konwersja kosztu na galeony, sykle i knuty
    galeon = koszt // 493
    reszta_galeony = koszt % 493
    sykl = reszta_galeony // 29
    knut = reszta_galeony % 29
    
    return {"galeon": galeon, "sykl": sykl, "knut": knut}

# Przykładowe wywołanie
wynik = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec')
print(wynik)

# Liczenie zad3
def licz_sume(dane_wejsciowe):
    # Przeliczniki
    przelicznik_sykli_na_geleony = 17
    przelicznik_knutow_na_sykli = 21

    # Podawanie liczby
    ilosc_geleonow = int(input("Podaj ilość geleonów: "))
    ilosc_sykli = int(input("Podaj ilość sykli: "))
    ilosc_knutow = int(input("Podaj ilość knutów: "))

    suma_knutow = ilosc_knutow + ilosc_sykli * przelicznik_knutow_na_sykli + ilosc_geleonow * przelicznik_sykli_na_geleony * przelicznik_knutow_na_sykli

    # Przeliczenie na monety o największym nominale
    ilosc_geleonow_po_przeliczeniu = suma_knutow // (przelicznik_sykli_na_geleony * przelicznik_knutow_na_sykli)
    suma_knutow %= przelicznik_sykli_na_geleony * przelicznik_knutow_na_sykli
    ilosc_sykli_po_przeliczeniu = suma_knutow // przelicznik_knutow_na_sykli
    suma_knutow %= przelicznik_knutow_na_sykli

    # Tworzenie wynikowego słownika
    wynik = {
        'geleon': ilosc_geleonow_po_przeliczeniu,
        'sykl': ilosc_sykli_po_przeliczeniu,
        'knut': suma_knutow
    }

    return wynik

# Powinno być git

# Przykładowe użycie funkcji
dane = {'geleon': 0, 'sykl': 0, 'knut': 0}
print(licz_sume(dane))
import time
import random

def wyslij_sowe(adresat, tresc_listu):
    print(f"Wysyłanie listu do {adresat}...")
    time.sleep(1)  # Odczekaj 1 sekundę

    # Zrandomizuj, czy operacja się powiedzie
    if random.random() < 0.9:
        print("Sowa wysłana pomyślnie!")
        return True
    else:
        print("Błąd podczas wysyłania sowy.")
        return False

# Przykładowe użycie funkcji
adresat = "Jan Kowalski"
tresc_listu = "Cześć Janek, jak się masz?"
powodzenie = wyslij_sowe(adresat, tresc_listu)
print("Operacja powiodła się:", powodzenie)

#Przetestowane, rzeczywiście raz na 10 razy sowa sie nie wysyla
