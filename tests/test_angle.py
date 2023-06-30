from src import angle


def test_twelve():
    assert angle.between("12:00") == 0


def test_three():
    assert angle.between("3:00") == 90


def test_five_thirty():
    assert angle.between("5:30") == 15
