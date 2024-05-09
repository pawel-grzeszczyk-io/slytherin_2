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