from yatzy import Yatzy

# These unit tests can be run using the py.test framework
# available from http://pytest.org/


def test_chance():
    assert 15 == Yatzy.chance(2, 3, 4, 5, 1)
    assert 16 == Yatzy.chance(3, 3, 4, 5, 1)


def test_yatzy():
    assert 50 == Yatzy.yatzy(4, 4, 4, 4, 4)

    assert 50 == Yatzy.yatzy(6, 6, 6, 6, 6)
    assert 0 == Yatzy.yatzy(6, 6, 6, 6, 3)


def test_ones():
    assert Yatzy.sameNumber(1, 1, 2, 3, 4, 5) == 1
    assert 2 == Yatzy.sameNumber(1, 1, 2, 1, 4, 5)
    assert 0 == Yatzy.sameNumber(1, 6, 2, 2, 4, 5)
    assert 4 == Yatzy.sameNumber(1, 1, 2, 1, 1, 1)


def test_twos():
    assert 4 == Yatzy.sameNumber(2, 1, 2, 3, 2, 6)
    assert 10 == Yatzy.sameNumber(2, 2, 2, 2, 2, 2)


def test_threes():
    assert 6 == Yatzy.sameNumber(3, 1, 2, 3, 2, 3)
    assert 12 == Yatzy.sameNumber(3, 2, 3, 3, 3, 3)


def test_fours():
    assert 12 == Yatzy.sameNumber(4, 4, 4, 4, 5, 5)
    assert 8 == Yatzy.sameNumber(4, 4, 4, 5, 5, 5)
    assert 4 == Yatzy.sameNumber(4, 4, 5, 5, 5, 5)


def test_fives():
    assert 10 == Yatzy.sameNumber(5, 4, 4, 4, 5, 5)
    assert 15 == Yatzy.sameNumber(5, 4, 4, 5, 5, 5)
    assert 20 == Yatzy.sameNumber(5, 4, 5, 5, 5, 5)


def test_sixes():
    assert 0 == Yatzy.sameNumber(6, 4, 4, 4, 5, 5)
    assert 6 == Yatzy.sameNumber(6, 4, 4, 6, 5, 5)
    assert 18 == Yatzy.sameNumber(6, 6, 5, 6, 6, 5)


def test_pair():
    assert 6 == Yatzy.amountOfAKind(2, 3, 4, 3, 5, 6)
    assert 10 == Yatzy.amountOfAKind(2, 5, 3, 3, 3, 5)
    assert 12 == Yatzy.amountOfAKind(2, 5, 3, 6, 6, 5)
    assert 12 == Yatzy.amountOfAKind(2, 5, 3, 6, 6, 6)


def test_three_of_a_kind():
    assert 9 == Yatzy.amountOfAKind(3, 3, 3, 3, 4, 5)
    assert 15 == Yatzy.amountOfAKind(3, 5, 3, 5, 4, 5)
    assert 9 == Yatzy.amountOfAKind(3, 3, 3, 3, 3, 5)


def test_four_of_a_knd():
    assert 12 == Yatzy.amountOfAKind(4, 3, 3, 3, 3, 5)
    assert 20 == Yatzy.amountOfAKind(4, 5, 5, 5, 4, 5)
    assert 12 == Yatzy.amountOfAKind(4, 3, 3, 3, 3, 3)
    assert 0 == Yatzy.amountOfAKind(4, 3, 3, 3, 2, 1)


def test_two_Pair():
    assert 16 == Yatzy.two_pair(3, 3, 5, 4, 5)
    assert 18 == Yatzy.two_pair(3, 3, 6, 6, 6)
    assert 0 == Yatzy.two_pair(3, 3, 6, 5, 4)


def test_smallStraight():
    assert 15 == Yatzy.smallStraight(1, 2, 3, 4, 5)
    assert 15 == Yatzy.smallStraight(2, 3, 4, 5, 1)
    assert 0 == Yatzy.smallStraight(1, 2, 2, 4, 5)


def test_largeStraight():
    assert 20 == Yatzy.largeStraight(6, 2, 3, 4, 5)
    assert 20 == Yatzy.largeStraight(2, 3, 4, 5, 6)
    assert 0 == Yatzy.largeStraight(1, 2, 2, 4, 5)


def test_fullHouse():
    assert 18 == Yatzy.fullHouse(6, 2, 2, 2, 6)
    assert 0 == Yatzy.fullHouse(2, 3, 4, 5, 6)
