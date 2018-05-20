# TourOperator
Simple simulator of tour operator with using OOP Python.

Documentation for using TourOperator simulator.

Класс Workers() из модуля Workers
Методы:
1. AddWorker(FirstName, LastName, Sex, Position, Department) - добавление нового работника с указанными данными в журнал self.Log
2. AddWorkers(*lsts) - добавление нескольких работников. В качестве аргументов передаются списки содержащие необходимые данные в порядке ввода аргументов метода AddWorker(FirstName, LastName, Sex, Position, Department)
3. DelWorker(FirstName, LastName, Sex, Position, Department) - удаление работника с указанными данными из журнала self.Log. Выводит предупреждение если журнал пуст или такого сотрудника не зарегистрировано
4. DelWorkers(*lsts) - удаление нескольких работников. В качестве аргументов передаются списки содержащие необходимые данные в порядке ввода аргументов метода DelWorker(FirstName, LastName, Sex, Position, Department)
5. ViewLog - просмотр данных журнала в удобном для чтения формате

Класс Clients() из модуля Clients
Методы:
1. AddClient(FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class) - добавление нового клиента с указанными данными в журнал self.Log
2. AddClients(*lsts) - добавление нескольких работников. В качестве аргументов передаются списки содержащие необходимые данные в порядке ввода аргументов метода AddClient(FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class)
3. DelClient(FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class) - удаление клиента с указанными данными из журнала self.Log. Выводит предупреждение если журнал пуст или такого клиента не зарегистрировано
4. DelClients(*lsts) - удаление нескольких клиентов. В качестве аргументов передаются списки содержащие необходимые данные в порядке ввода аргументов метода DelClient(FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class)
5. ViewLog - просмотр данных журнала в удобном для чтения формате

Класс Deals() из модуля Deals
Методы:
1. addDeal(self, FirstName, LastName, Passport, Email, PhoneNumber, HostCountry, HostCity, Class) - добавление заказа тура в журнал self.Log. Выводит предупреждение если такого клиента не зарегистрировано
2. ViewLog - просмотр данных журнала в удобном для чтения формате


Модуль main
Создание объектов всех неободимых классов и работа с ними.
В качестве примера работы с симулятором использованы основные методы классов Workers(), Clients(), Deals()
