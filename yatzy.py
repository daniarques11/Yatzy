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
    def ones(*dice):
        sum = 0
        for die in dice:
            if die == 1:
                sum += 1
        return sum

    @staticmethod
    def twos(*dice):
        sum = 0
        for die in dice:
            if die == 2:
                sum += 2
        return sum

    @staticmethod
    def threes(*dice):
        sum = 0
        for die in dice:
            if die == 3:
                sum += 3
        return sum

    @staticmethod
    def fours(*dice):
        sum = 0
        for die in dice:
            if die == 4:
                sum += 4
        return sum

    @staticmethod
    def fives(*dice):
        sum = 0
        for die in dice:
            if die == 5:
                sum += 5
        return sum

    @staticmethod
    def sixes(*dice):
        sum = 0
        for die in dice:
            if die == 6:
                sum += 6
        return sum

    @staticmethod
    def pair(*dice):
        for number in range(6, 0, -1):
            if dice.count(number) >= 2:
                return number*2
        return 0

    @staticmethod
    def threeOfAKind(*dice):
        for number in range(6, 0, -1):
            if dice.count(number) >= 3:
                return number*3
        return 0

    @staticmethod
    def fourOfAKind(*dice):
        for number in range(6, 0, -1):
            if dice.count(number) >= 4:
                return number*4
        return 0

    @staticmethod
    def twoPair(*dice):
        numberOfPairs = 0
        points = 0
        for number in range(6, 0, -1):
            if dice.count(number) >= 2:
                numberOfPairs += 1
                points += number*2

        if (numberOfPairs >= 2):
            return points
        else:
            return 0

    @staticmethod
    def smallStraight(*dice):
        for number in range(1, 5):
            if number not in dice:
                return 0
        return 15

    @staticmethod
    def largeStraight(*dice):
        for number in range(2, 6):
            if number not in dice:
                return 0
        return 20

    @staticmethod
    def fullHouse(*dice):
        diceCountList = [0]*6

        for die in dice:
            diceCountList[die-1] += 1

        score = 0
        threeOfAKindExists = False
        pairExists = False
        for dieMinusOne, dieCount in enumerate(diceCountList):
            if dieCount == 3:
                score += (dieMinusOne + 1) * 3
                threeOfAKindExists = True
            if dieCount == 2:
                score += (dieMinusOne + 1) * 2
                pairExists = True

        if pairExists and threeOfAKindExists:
            return score
        else:
            return 0
