from collections import OrderedDict
import json


class Workers:

    def AddWorker(self, FirstName, LastName, Sex, Position, Department):
        try:
            with open('TourOperator[Workers].json', 'r') as file:
                data = json.loads(file.read())
                if (FirstName not in data['FirstNames']) or \
                   (LastName not in data['LastNames']) or \
                   (Sex not in data['Sex']) or \
                   (Position not in data['Positions']) or \
                   (Department not in data['Departments']):
                    with open('TourOperator[Workers].json', 'w') as file:
                        data['FirstNames'].append(FirstName)
                        data['LastNames'].append(LastName)
                        data['Sex'].append(Sex)
                        data['Positions'].append(Position)
                        data['Departments'].append(Department)
                        json.dump(data, file)
                    print('Сотрудник с такими данными был(-ла) успешно добавлен(-на) в журнал.')
                elif (FirstName in data['FirstNames']) and \
                     (LastName in data['LastNames']) and \
                     (Sex in data['Sex']) and \
                     (Position in data['Positions']) and \
                     (Department in data['Departments']):
                    print('Сотрудник с введенными данными уже был(-ла) ранее зарегистрирован(-на).')
        except FileNotFoundError:
            with open('TourOperator[Workers].json', 'w') as file:
                data = OrderedDict({'FirstNames': [FirstName],
                                    'LastNames': [LastName],
                                    'Sex': [Sex],
                                    'Positions': [Position],
                                    'Departments': [Department]})
                json.dump(data, file)
            print('Сотрудник с такими данными был(-ла) успешно добавлен(-на) в журнал.')

    def AddWorkers(self, *lsts):
        for worker_data in lsts:
            self.AddWorker(*worker_data)

    def DelWorker(self, FirstName, LastName, Sex, Position, Department):
        dct = {'FirstNames': FirstName,
               'LastNames': LastName,
               'Sex': Sex,
               'Positions': Position,
               'Departments': Department}
        lstVars = list(dct.keys())
        lstFirstNames, lstLastNames, lstSex, lstPositions, lstDepartments = [], [], [], [], []
        numbers = []

        try:
            with open('TourOperator[Workers].json', 'r') as f:
                data = json.loads(f.read())
                assert len(data['FirstNames']), 'Журнал пуст, сначала добавьте сотрудника(-ов).'
                for i in range(len(data['FirstNames'])):
                    for j in lstVars:
                        if dct[j] == data[j][i]:
                            eval(f'lst{j}.append(i)')

                for i in lstFirstNames:
                    if (i in lstLastNames) and (i in lstSex) and (i in lstPositions) and (i in lstDepartments) and (not i in numbers):
                        numbers.append(i)

                try:
                    assert len(numbers), 'Сотрудника с такими данными не зарегистрировано.'
                    with open('TourOperator[Workers].json', 'w') as file:
                        for i in numbers:
                            for j in lstVars:
                                del data[j][i]
                        json.dump(data, file)
                    print('Сотрудник с такими данными был(-ла) успешно удален(-на) из журнала.')

                except AssertionError as err:
                    print(err)

        except AssertionError as err:
            print(err)

    def DelWorkers(self, *lsts):
        for worker_data in lsts:
            self.DelWorker(*worker_data)

    @property
    def ViewLog(self):
        with open('TourOperator[Workers].json', 'r') as f:
            data = json.loads(f.read())
            lstHeads = ['FirstNames', 'LastNames', 'Sex', 'Positions', 'Departments']
            gaps = 63
            print('∧' * gaps, '\n', '{:>45}'.format('\033[1mLOG OF WORKERS'), '\n')
            print('{0:15} {1:15} {2:10} {3:15} {4:}\033[0m'.format(*lstHeads))
            for i in range(len(data['FirstNames'])):
                print('{0:15} {1:15} {2:10} {3:15} {4:}'.format(data['FirstNames'][i],
                                                                data['LastNames'][i],
                                                                data['Sex'][i],
                                                                data['Positions'][i],
                                                                data['Departments'][i], '\n'))
            print(f"\nИтого: \033[1m{len(data['FirstNames'])}\033[0m сотрудников(-а)")
            print('∨' * gaps)

    def _getLog(self):
        with open('TourOperator[Workers].json', 'r') as f:
            data = json.loads(f.read())
            return data
