def waluta_dict_na_str(waluta_dict: dict):
    # Słownik odmiany poszczególnych walut
    waluty = {
        'galeon' : ['galeony', 'galeonów'],
        'sykl' : ['sykle', 'sykli'],
        'knut' : ['knuty', 'knutów']
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
    print(waluta_str.strip())
