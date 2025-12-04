import main

def test_result():
    bank = main.BankInterest(100000, 2, 10)
    assert len(bank.ann_int()) == 2
    assert bank.ann_int() == (4614.49, 110747.82)