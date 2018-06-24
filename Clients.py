from collections import OrderedDict
import json


class Clients:

    def AddClient(self, FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class):
        try:
            with open('TourOperator[Clients].json', 'r') as file:
                data = json.loads(file.read())
                if (FirstName not in data['FirstNames']) or \
                   (LastName not in data['LastNames']) or \
                   (Passport not in data['Passports']) or \
                   (EMail not in data['EMails']) or \
                   (PhoneNumber not in data['PhoneNumbers']) or \
                   (HostCountry not in data['HostContries']) or \
                   (HostCity not in data['HostCities']) or \
                   (Class not in data['Classes']):
                    with open('TourOperator[Clients].json', 'w') as file:
                        data['FirstNames'].append(FirstName)
                        data['LastNames'].append(LastName)
                        data['Passports'].append(Passport)
                        data['EMails'].append(EMail)
                        data['PhoneNumbers'].append(PhoneNumber)
                        data['HostContries'].append(HostCountry)
                        data['HostCities'].append(HostCity)
                        data['Classes'].append(Class)
                        json.dump(data, file)
                    print('Клиент с такими данными был(-ла) успешно добавлен(-на) в журнал.')
                elif (FirstName in data['FirstNames']) and \
                     (LastName in data['LastNames']) and \
                     (Passport in data['Passports']) and \
                     (EMail in data['EMails']) and \
                     (PhoneNumber in data['PhoneNumbers']) and \
                     (HostCountry in data['HostContries']) and \
                     (HostCity in data['HostCities']) and \
                     (Class in data['Classes']):
                    print('Клиент с введенными данными уже был(-ла) ранее зарегистрирован(-на).')
        except FileNotFoundError:
            with open('TourOperator[Clients].json', 'w') as file:
                data = OrderedDict({'FirstNames': [FirstName],
                                    'LastNames': [LastName],
                                    'Passports': [Passport],
                                    'EMails': [EMail],
                                    'PhoneNumbers': [PhoneNumber],
                                    'HostContries': [HostCountry],
                                    'HostCities': [HostCity],
                                    'Classes': [Class]})
                json.dump(data, file)
            print('Клиент с такими данными был(-ла) успешно добавлен(-на) в журнал.')

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
            with open('TourOperator[Clients].json', 'r') as f:
                data = json.loads(f.read())
                assert len(data['FirstNames']) > 0, 'Журнал пуст, сначала добавьте клиента(-ов).'
                for i in range(len(data['FirstNames'])):
                    for j in lstVars:
                        if dct[j] == data[j][i]:
                            eval(f'lst{j}.append(i)')

                for i in lstFirstNames:
                    if (i in lstLastNames) and (i in lstPassports) and (i in lstEMails) and (i in lstPhoneNumbers) and (i in lstHostCountries)  and (i in lstHostCities)  and (i in lstClasses) and (not i in numbers):
                        numbers.append(i)

                try:
                    assert len(numbers), 'Клиента с такими данными не зарегистрировано.'
                    with open('TourOperator[Clients].json', 'w') as file:
                        for i in numbers:
                            for j in lstVars:
                                del data[j][i]
                        json.dump(data, file)
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
        with open('TourOperator[Clients].json', 'r') as f:
            data = json.loads(f.read())
            lstHeads = ['FirstNames', 'LastNames', 'Passports', 'Emails', 'PhoneNumbers', 'HostCountries', 'HostCities', 'Classes']
            gaps = 120
            print('∧' * gaps, '\n', '{:>80}'.format('\033[1mLOG OF CLIENTS'), '\n')
            print('{0:15} {1:15} {2:15} {3:30} {4:20} {5:15} {6:15} {7:15}\033[0m'.format(*lstHeads))
            for i in range(len(data['FirstNames'])):
                print('{0:15} {1:15} {2:15} {3:30} {4:20} {5:15} {6:15} {7:15}'.format(data['FirstNames'][i],
                                                                                       data['LastNames'][i],
                                                                                       data['Passports'][i],
                                                                                       data['EMails'][i],
                                                                                       data['PhoneNumbers'][i],
                                                                                       data['HostCountries'][i],
                                                                                       data['HostCities'][i],
                                                                                       data['Classes'][i], '\n'))
            print(f"\nИтого: \033[1m{len(data['FirstNames'])}\033[0m клиента(-ов)")
            print('∨' * gaps)

    def _getLog(self):
        with open('TourOperator[Clients].json', 'r') as f:
            data = json.loads(f.read())
            return data
