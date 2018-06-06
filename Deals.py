from Workers import Workers
from Clients import Clients
from random import randint
import json


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

            if Class == 'First Class' or Class == 'First-Class':
                price = coefficient * constFirstClass
            elif Class == 'Business Class' or Class == 'Business-Class':
                price = coefficient * constBusinessClass
            elif Class == 'Economy Class' or Class == 'Economy-Class':
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

            try:
                with open('TourOperator[Deals].json', 'r') as file:
                    data = json.loads(file.read())
                    for i in data:
                        if lstWorker == i[0]:
                            ind = data.index(i)
                            break
                    else:
                        ind = -1
            except FileNotFoundError:
                with open('TourOperator[Deals].json', 'w') as file:
                    data = []
                    json.dump(data, file)
                    ind = -1
            with open('TourOperator[Deals].json', 'r') as file1:
                data = json.loads(file1.read())
                with open('TourOperator[Deals].json', 'w') as file2:
                    if ind >= 0:
                        data[ind].append(lstClient)
                    elif ind == -1:
                        data.append([lstWorker, lstClient])
                    json.dump(data, file2)
                    print('Сделка была успешно добавлена в журнал.')
        except AssertionError as err:
            print(err)

    @property
    def ViewLog(self):
        lstHeads = ['Workers', 'Clients', 'Price', 'Result']
        gaps = 160
        print('∧' * gaps, '\n', '{:>115}'.format('\033[1mLOG OF DEALS'), '\n')
        print('{0:60} {1:120} {2:10} {3:10}\033[0m'.format(*lstHeads))
        with open('TourOperator[Deals].json', 'r') as file:
            data = json.loads(file.read())
            for info in data:
                print('{0:60} {1:120} {2:10} {3:10}'.format(str(info[0]), str(info[1][:-2]), str(info[1][-2]) + "$", info[1][-1]))
                if len(info) > 2:
                    for i in info[2:]:
                        print('{0:>178} {1:>10} {2:>10}'.format(str(i[:-2]), str(i[-2]) + "$", i[-1]))
            print('∨' * gaps)
