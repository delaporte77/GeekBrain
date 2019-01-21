import random


class gameInit:

    @staticmethod
    def game():

        n = range(1, 90)
        barrelList = random.sample(n, 27)

        barrelList.sort()

        for i in range(11):
            barrelList[(random.randint(0, 26))] = ' '

        return barrelList


class showTicket:

    def __init__(self, numbers):
        self.numbers = numbers

    def createTicket(self):

        #ticket = """
        #-----------------------------------------
        ##{0}
        #{1}
        #{2}
        #-----------------------------------------
        #""".format(self.numbers[0:8],self.numbers[9:16],self.numbers[17:26])

        return self.numbers

def game():

    numList = gameInit.game()
    programm = showTicket(numList)
    computerTicket = programm.createTicket()

    numList = gameInit.game()
    programm = showTicket(numList)
    userTicket = programm.createTicket()

    userScore = 0
    computerScore = 0


    while userScore != 15 or computerScore != 15:


        print('Билет пользователя: ' + str(userTicket))

        userAsk = input('Введите вашу цифру:')

        if int(userAsk) in userTicket:
            userTicket[userTicket.index(int(userAsk))] = '-'
            userScore += 1

        computerAsk = random.randint(0, 26)

        print('Билет компьютера: ' + str(computerTicket))
        print('Компьютер выбрал цифру %s' %computerAsk)

        if int(computerAsk) in computerTicket:
            computerTicket[computerTicket.index(int(computerAsk))] = '-'
            computerScore += 1


game()