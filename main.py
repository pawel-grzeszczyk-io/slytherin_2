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