from main import waluta_str_na_dict

def test_waluta_str_na_dict():
    x = waluta_str_na_dict("13 knut")
    y = waluta_str_na_dict("17 galeon 2 sykl 13 knut")

    assert x == { "galeon" : 0, "sykl" : 0, "knut" : 13}
    assert y == {'galeon': 17, 'sykl': 2, 'knut': 13}
    