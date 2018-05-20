from collections import OrderedDict


class Workers:

    def __init__(self, Log = OrderedDict({'FirstNames': [], 'LastNames': [], 'Sex': [], 'Positions': [], 'Departments': []})):
        self.Log = Log

    def AddWorker(self, FirstName, LastName, Sex, Position, Department):
        dct = {'FirstNames': FirstName,
               'LastNames': LastName,
               'Sex': Sex,
               'Positions': Position,
               'Departments': Department}
        for key, value in dct.items():
            self.Log[key].append(value)

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
            assert len(self.Log['FirstNames']), 'Журнал пуст, сначала добавьте сотрудника(-ов).'
            for i in range(len(self.Log['FirstNames'])):
                for j in lstVars:
                    if dct[j] == self.Log[j][i]:
                        eval(f'lst{j}.append(i)')

            for i in lstFirstNames:
                if (i in lstLastNames) and (i in lstSex) and (i in lstPositions) and (i in lstDepartments) and (not i in numbers):
                    numbers.append(i)

            try:
                assert len(numbers), 'Сотрудника с такими данными не зарегистрировано.'
                for i in numbers:
                    for j in lstVars:
                        del self.Log[j][i]
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
        lstHeads = ['FirstNames', 'LastNames', 'Sex', 'Positions', 'Departments']
        gaps = 63
        print('∧' * gaps, '\n', '{:>45}'.format('\033[1mLOG OF WORKERS'), '\n')
        print('{0:15} {1:15} {2:10} {3:15} {4:}\033[0m'.format(*lstHeads))
        for i in range(len(self.Log['FirstNames'])):
            print('{0:15} {1:15} {2:10} {3:15} {4:}'.format(self.Log['FirstNames'][i],
                                                            self.Log['LastNames'][i],
                                                            self.Log['Sex'][i],
                                                            self.Log['Positions'][i],
                                                            self.Log['Departments'][i], '\n'))
        print(f"\nИтого: \033[1m{len(self.Log['FirstNames'])}\033[0m сотрудников(-а)")
        print('∨' * gaps)

    def _getLog(self): return self.Log
