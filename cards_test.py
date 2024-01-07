import cards

def test_make_card_3():
    expected = (3, "Heart", "3 of Heart", "3H")
    actual = cards.make_cards(3,"Heart")
    assert actual == expected


def test_make_card_10():
    expected = (10, "Heart", "10 of Heart", "10H")
    actual = cards.make_cards(10,"Heart")
    assert actual == expected


def test_make_card_11():
    expected = (11, "Club", "11 of Club", "11C")
    actual = cards.make_cards(11,"Club")
    assert actual == expected


def test_make_card_12():
    expected = (12, "Heart", "12 of Heart", "12H")
    actual = cards.make_cards(12,"Heart")
    assert actual == expected


def test_make_card_13():
    expected = (13, "Spade", "13 of Spade", "13S")
    actual = cards.make_cards(13,"Spade")
    assert actual == expected


def test_make_card_14():
    expected = (14, "Diamon", "14 of Diamond", "14D")
    actual = cards.make_cards(14,"Diamond")
    assert actual == expected





deck = cards.make_deck()

def test_make_card_invalid():
    expected = None
    actual = cards.make_cards(5,"yumm")
    assert actual == expected

def test_shuffle():
    cards.shuffle(deck)
    assert deck[0] != (11,"Club","Jack of Club", "JC")

def test_shuffle():
    cards.shuffle(deck)
    assert deck[51] != (14,"Spade","Ace of Spade", "AS")




