
def waluta_str_na_dict(input_str):
    # Słownik z wartościami domyślnymi dla każdego typu monety
    currency_dict = {
        "galeon": 0,
        "sykl": 0,
        "knut": 0
    }
    
    # Przeliczniki monet
    galeon_to_knut = 17 * 21  # 1 galeon = 17 sykli, 1 sykl = 21 knutów
    sykl_to_knut = 21
    galeon_to_sykl = 17
    
    # Dzielimy wejściowy ciąg znaków na elementy
    parts = input_str.split()
    
    # Zmienna do przechowywania sumy wartości w knutach
    total_knuts = 0
    
    # Iterujemy po elementach, przeskakując co dwa elementy (liczba, typ monety)
    for i in range(0, len(parts), 2):
        amount = int(parts[i])  # Konwersja liczby na integer
        currency_type = parts[i + 1].lower()  # Typ monety
        
        # Przypisz wartość do odpowiedniego klucza w słowniku
        if currency_type.startswith('g'):
            currency_dict["galeon"] = amount
            total_knuts += amount * galeon_to_knut
        elif currency_type.startswith('s'):
            currency_dict["sykl"] = amount
            total_knuts += amount * sykl_to_knut
        elif currency_type.startswith('k'):
            currency_dict["knut"] = amount
            total_knuts += amount
    
    
    return currency_dict
print(waluta_str_na_dict("13 knut"))
print(waluta_str_na_dict("17 galeon 100 sykl 13 k"))