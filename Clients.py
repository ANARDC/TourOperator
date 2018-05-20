from collections import OrderedDict


class Clients:

    def __init__(self, Log = OrderedDict({"FirstNames": [], "LastNames": [], "Passports": [], "EMails": [], "PhoneNumbers": [],"HostCountries": [], "HostCities": [], "Classes": []})):
        self.Log = Log

    def AddClient(self, FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class):
        dct = {'FirstNames': FirstName,
               'LastNames': LastName,
               'Passports': Passport,
               'EMails': EMail,
               'PhoneNumbers': PhoneNumber,
               'HostCountries': HostCountry,
               'HostCities': HostCity,
               'Classes': Class}

        for key, value in dct.items():
            self.Log[key].append(value)

        print('Клиент с такими данными был успешно добавлен в журнал.')

    def AddClients(self, *lsts):
        for client_data in lsts:
            self.AddClient(*client_data)

    def DelClient(self, FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class):
        dct = {'FirstNames': FirstName,
               'LastNames': LastName,
               'Passports': Passport,
               'EMails': EMail,
               'PhoneNumbers': PhoneNumber,
               'HostCountries': HostCountry,
               'HostCities': HostCity,
               'Classes': Class}

        lstVars = list(dct.keys())
        lstFirstNames, lstLastNames, lstPassports, lstEMails, lstPhoneNumbers, lstHostCountries, lstHostCities, lstClasses = [], [], [], [], [], [], [], []
        numbers = []

        try:
            assert len(self.Log['FirstNames']) > 0, 'Журнал пуст, сначала добавьте клиента(-ов).'
            for i in range(len(self.Log['FirstNames'])):
                for j in lstVars:
                    if dct[j] == self.Log[j][i]:
                        eval(f'lst{j}.append(i)')

            for i in lstFirstNames:
                if (i in lstLastNames) and (i in lstPassports) and (i in lstEMails) and (i in lstPhoneNumbers) and (i in lstHostCountries)  and (i in lstHostCities)  and (i in lstClasses) and (not i in numbers):
                    numbers.append(i)

            try:
                assert len(numbers), 'Клиента с такими данными не зарегистрировано.'
                for i in numbers:
                    for j in lstVars:
                        del self.Log[j][i]
                print('Клиент с такими данными был(-ла) успешно удален(-на) из журнала.')

            except AssertionError as err:
                print(err)

        except AssertionError as err:
            print(err)

    def DelClients(self, *lsts):
        for client_data in lsts:
            self.DelClient(*client_data)

    @property
    def ViewLog(self):
        lstHeads = ['FirstNames', 'LastNames', 'Passports', 'Emails', 'PhoneNumbers', 'HostCountries', 'HostCities', 'Classes']
        gaps = 120
        print('∧' * gaps, '\n', '{:>80}'.format('\033[1mLOG OF CLIENTS'), '\n')
        print('{0:15} {1:15} {2:15} {3:30} {4:20} {5:15} {6:15} {7:15}\033[0m'.format(*lstHeads))
        for i in range(len(self.Log['FirstNames'])):
            print('{0:15} {1:15} {2:15} {3:30} {4:20} {5:15} {6:15} {7:15}'.format(self.Log['FirstNames'][i],
                                                                                   self.Log['LastNames'][i],
                                                                                   self.Log['Passports'][i],
                                                                                   self.Log['EMails'][i],
                                                                                   self.Log['PhoneNumbers'][i],
                                                                                   self.Log['HostCountries'][i],
                                                                                   self.Log['HostCities'][i],
                                                                                   self.Log['Classes'][i], '\n'))
        print(f"\nИтого: \033[1m{len(self.Log['FirstNames'])}\033[0m клиента(-ов)")
        print('∨' * gaps)

    def _getLog(self): return self.Log
