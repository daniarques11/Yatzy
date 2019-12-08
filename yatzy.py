class Yatzy:

    @staticmethod
    def chance(*dice):
        total = 0
        for numero in dice:
            total += numero
        return total

    @staticmethod
    def yatzy(*dice):
        if dice.count(dice[0]) == len(dice):
            return 50
        return 0

    @staticmethod
    def sameNumber(dieCategory, *dice):
        sum = 0
        for die in dice:
            if die == dieCategory:
                sum += dieCategory
        return sum

    @staticmethod
    def score_pair(*dice):
        for number in range(6, 1, -1):
            if dice.count(number) >= 2:
                return number*2
        return 0

    @staticmethod
    def two_pair(*dice):
        numberOfPairs = 0
        points = 0
        for number in range(6, 1, -1):
            if dice.count(number) >= 2:
                numberOfPairs += 1
                points += number*2

        if (numberOfPairs >= 2):
            return points
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i+1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i+1) * 3
        return 0

    @staticmethod
    def smallStraight(d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i+1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i+1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
