from Workers import Workers
from Clients import Clients
from random import randint


class _WorkersInfo(Workers):
    getLogWorkers = Workers._getLog

    def _getInfo(self):
        for i, k in self.getLogWorkers().items():
            print(i, k)


class _ClientsInfo(Clients):
    getLogClients = Clients._getLog

    def _getInfo(self):
        for i, k in self.getLogClients().items():
            print(i, k)


class Deals(_WorkersInfo, _ClientsInfo):
    def __init__(self):
        self.Log = []

    def addDeal(self, FirstName, LastName, Passport, Email, PhoneNumber, HostCountry, HostCity, Class):
        try:
            data = _WorkersInfo().getLogWorkers()
            assert len(data['FirstNames']), 'Ни одного работника не зарегистрировано.'
            number = randint(0, len(data['FirstNames']) - 1)
            lstWorker = []
            for i in list(data.values()):
                lstWorker.append(i[number])
        except AssertionError as err:
            print(err)

        try:
            lstClient = [FirstName, LastName, Passport, Email, PhoneNumber, HostCountry, HostCity, Class]
            data = list(_ClientsInfo().getLogClients().values())
            assert (FirstName in data[0]) and (LastName in data[1]) and (Passport in data[2]), 'Клиента с такими данными не зарегистрировано.'
            constFirstClass, constBusinessClass, constEconomyClass = 70, 45, 20
            coefficient = 44.9

            if Class == 'First Class':
                price = coefficient * constFirstClass
            elif Class == 'Business Class':
                price = coefficient * constBusinessClass
            elif Class == 'Economy Class':
                price = coefficient * constEconomyClass
            lstClient.append(price)

            def result():
                print(f'Рассчитанная цена равна {price}$ или {price * 68}₽\n')
                choice = input('Вы согласны купить тур по предоставленной сумме?(\033[1mДа/Нет\033[0m)\n')
                if choice == 'Да':
                    lstClient.append('Success')
                elif choice == 'Нет':
                    lstClient.append('Loss')
                else:
                    print('''Напишите еще раз свой выбор - "\033[1mДа\033[0m" или "\033[1mНет\033[0m"?''')
                    result()

            result()

            for i in self.Log:
                if lstWorker == i[0]:
                    ind = self.Log.index(i)
                    break
            else:
                ind = -1

            if ind >= 0:
                self.Log[ind].append(lstClient)
            elif ind == -1:
                self.Log.append([lstWorker, lstClient])
        except AssertionError as err:
            print(err)

    @property
    def ViewLog(self):
        lstHeads = ['Workers', 'Clients', 'Price', 'Result']
        gaps = 160
        print('∧' * gaps, '\n', '{:>115}'.format('\033[1mLOG OF DEALS'), '\n')
        print('{0:60} {1:120} {2:10} {3:10}\033[0m'.format(*lstHeads))
        for data in self.Log:
            print('{0:60} {1:120} {2:10} {3:10}'.format(str(data[0]), str(data[1][:-2]), str(data[1][-2]) + "$", data[1][-1]))
            if len(data) > 2:
                for i in data[2:]:
                    print('{0:>178} {1:>10} {2:>10}'.format(str(i[:-2]), str(i[-2]) + "$", i[-1]))
        print('∨' * gaps)
