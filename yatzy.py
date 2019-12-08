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
    def amountOfAKind(amount, *dice):
        for number in range(6, 0, -1):
            if dice.count(number) >= amount:
                return number*amount
        return 0

    @staticmethod
    def two_pair(*dice):
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
        diceList = []
        points = 0
        for die in dice:
            diceList.append(die)
        for number in range(6, 0, -1):
            if diceList.count(number) >= 3:
                points += number*3
                while number in diceList:
                    diceList.remove(number)
        for number in range(6, 0, -1):
            if diceList.count(number) >= 2:
                points += number*2
        return points
