import time
import random
import csv
from datetime import datetime
import pandas as pd

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
# wynik = wybierz_sowe_zwroc_koszt(True, 'lokalna', 'list', 'wyjec')
# print(wynik)

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
# Przykładowe użycie funkcji
# dane = {'geleon': 0, 'sykl': 0, 'knut': 0}
# print(licz_sume(dane))

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
# adresat = "Jan Kowalski"
# tresc_listu = "Cześć Janek, jak się masz?"
# powodzenie = wyslij_sowe(adresat, tresc_listu)
# print("Operacja powiodła się:", powodzenie)

def waluta_dict_na_str(waluta_dict: dict):
    # Słownik odmiany poszczególnych walut
    waluty = {
        'galeon': ['galeony', 'galeonów'],
        'sykl': ['sykle', 'sykli'],
        'knut': ['knuty', 'knutów']
    }

    # Zmienna do przechowywania wyniku konwersji
    waluta_str = ''

    # Iteruje po kluczach (waluta) i wartościach (wartosc) słownika
    for waluta, wartosc in waluta_dict.items():

        # Jeśli waluta nie jest na liście walut - zwróć błąd
        if waluta not in waluty.keys():
            raise ValueError('Podano nieprawidłową walutę')

        # Jeśli wartość nie jest liczbą całkowitą - zwróć błąd
        if not isinstance(wartosc, int):
            raise TypeError('Wartości nominałów muszą być liczbami całkowitymi')

        # Jeśli wartość jest mniejsza od 0 - zwróć błąd
        if wartosc < 0:
            raise ValueError('Wartości nominałów nie mogą być mniejsze od 0')

        # Jeśli wartość jest równa 0 - pominń
        elif wartosc == 0:
            continue

        # Jeśli wartość jest równa 1 - zwróć z domyślnym formatowaniem waluty
        elif wartosc == 1:
            waluta_str += f' {wartosc} {waluta}'

            # Jeśli wartość jest większa od 1 - zwróć z poprawionym formatowaniem (na podstawie `waluty`)
        else:
            if wartosc < 5:
                new_waluta = waluty[waluta][0]
            else:
                new_waluta = waluty[waluta][1]

            waluta_str += f' {wartosc} {new_waluta}'

            # Wyprintuj ostateczny wynik
    return waluta_str.strip()

def nadaj_sowe(adresat, tresc_wiadomosci, potwierdzenie_odbioru, odleglosc, typ, specjalna):
    koszt_przesylki = wybierz_sowe_zwroc_koszt(potwierdzenie_odbioru, odleglosc, typ, specjalna)
    koszt_str = waluta_dict_na_str(koszt_przesylki)
    potwierdzenie_str = "TAK" if potwierdzenie_odbioru else "NIE"

    with open('poczta_nadania_lista.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([adresat, tresc_wiadomosci, koszt_str, potwierdzenie_str])

nadaj_sowe("Zuza", "Testujemy czy system nam dziala", True, 'lokalna', 'list', 'wyjec')



def poczta_wyslij_sowy(sciezka_do_pliku):
    column_names = ['adresat', 'treść wiadomości', 'koszt przesyłki', 'potwierdzenie odbioru']
    data = pd.read_csv(sciezka_do_pliku, encoding='latin1', header=None, names=column_names)
    wyniki = []
    for index, wiersz in data.iterrows():
        adresat = wiersz['adresat']
        tresc_listu = wiersz['treść wiadomości']
        koszt_przesylki = wiersz['koszt przesyłki']
        potwierdzenie_odbioru = wiersz['potwierdzenie odbioru']

        wysylka_sowy = wyslij_sowe(adresat, tresc_listu)
        if wysylka_sowy or potwierdzenie_odbioru == "TAK":
            rzeczywisty_koszt = 0
        else:
            rzeczywisty_koszt = koszt_przesylki

        wyniki.append({
            'adresat': adresat,
            'tresc wiadomosci': tresc_listu,
            'koszt przesylki': koszt_przesylki,
            'potwierdzenie odbioru': potwierdzenie_odbioru,
            'rzeczywisty koszt': rzeczywisty_koszt
        })

    wyniki_df = pd.DataFrame(wyniki)
    wyniki_df.to_csv('output_sowy_z_poczty_dzien_miesiac_rok.csv')

    
poczta_wyslij_sowy('poczta_nadania_lista.csv')


