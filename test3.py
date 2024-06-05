from main import licz_sume

def test_licz_sume():
    x = licz_sume({'galeon': [0], 'sykl': [0], 'knut': [0]}) # tst1 - wszystkie wartości to zero
    y = licz_sume({'galeon': [1], 'sykl': [1], 'knut': [1]})  # tst2 - mieszane wartości, ale nie trzeba przeliczać
    z = licz_sume({'galeon': [0], 'sykl': [0], 'knut': [10]})  # tst3 - same knuty
    w = licz_sume({'galeon': [0], 'sykl': [1], 'knut': [0]}) # tst4 - same sykle
    u = licz_sume({'galeon': [1], 'sykl': [0], 'knut': [0]}) # tst5 - same galeony
    v = licz_sume({'galeon': [2], 'sykl': [18], 'knut': [22]}) # tst6 - mieszane większe wartości, trzeba przeliczyć

    assert x == {'geleon': 0, 'sykl': 0, 'knut': 0}
    assert y == {'geleon': 1, 'sykl': 1, 'knut': 1}
    assert z == {'geleon': 0, 'sykl': 0, 'knut': 10}
    assert w == {'geleon': 0, 'sykl': 1, 'knut': 0}
    assert u == {'geleon': 1, 'sykl': 0, 'knut': 0}
    assert v == {'geleon': 3, 'sykl': 2, 'knut': 1}
