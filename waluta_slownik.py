import json

def waluta_str_na_dict(ciag):
    # Inicjalizacja słownika na ceny
    ceny = {"galeon": 0, "sykl": 0, "knut": 0}

    # Podział ciągu po spacji
    elementy = ciag.split()

    # Iteracja po indeksach i elementach listy
    for i in range(0, len(elementy), 2):
        # Rozdzielanie ilości i typu waluty
        ilosc = int(elementy[i])
        waluta = elementy[i + 1]

        # Sprawdzenie typu waluty i przypisanie odpowiedniej wartości
        if waluta.startswith('g'):
            ceny["galeon"] = ilosc
        elif waluta.startswith('s'):
            ceny["sykl"] = ilosc
        elif waluta.startswith('k'):
            ceny["knut"] = ilosc

    # Wypisanie ilości galeonów i syklów
    formatted_output = json.dumps(ceny, indent=4)
    print(formatted_output)

    return ceny

# Przykładowe wejścia i wyjścia
waluta_str_na_dict("13 knut")  # {'galeon': 0, 'sykl': 0, 'knut': 13}
waluta_str_na_dict("17 galeon 2 sykl 13 knut")  # {'galeon': 17, 'sykl': 2, 'knut': 13}

#D