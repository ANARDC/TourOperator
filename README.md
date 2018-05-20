# TourOperator
Simple simulator of tour operator with using OOP Python.

Documentation for using TourOperator simulator.

# Условие

Создать программу, которая будет симулировать работу туроператора.

Должны присутствовать классы сотрудников, клиентов, совершенных сделок и т.д.

Программа должна выводить историю совершенных покупок клиентом, продаж одного сотрудника, количество продаж по дням, туры в определенный срок и т.д.(доп. функционал можете продумать сами).

Я, как клиент, могу зарегистрироваться (т.е. создать объект имени меня) и "купить" тур


# Примечание

1. В задаче рассмотрены только клиенты без детей и жены/мужа

   При необходимости код может быть обновлен с учетом этих условий

2. В задаче рассмотрены постоянные константы для рассчета стоимости тура

   При необходимости код может быть обновлен с учетом определенных коэффициентов для разных стран и иных условий

## Класс Workers() из модуля Workers

Методы:

1. `**AddWorker(FirstName, LastName, Sex, Position, Department)**` - добавление нового работника с указанными данными в журнал self.Log

2. **AddWorkers(*lsts)** - добавление нескольких работников. В качестве аргументов передаются списки содержащие необходимые данные в порядке ввода аргументов метода AddWorker(FirstName, LastName, Sex, Position, Department)

3. DelWorker(FirstName, LastName, Sex, Position, Department) - удаление работника с указанными данными из журнала self.Log. Выводит предупреждение если журнал пуст или такого сотрудника не зарегистрировано

4. DelWorkers(*lsts) - удаление нескольких работников. В качестве аргументов передаются списки содержащие необходимые данные в порядке ввода аргументов метода DelWorker(FirstName, LastName, Sex, Position, Department)

5. ViewLog - просмотр данных журнала в удобном для чтения формате

## Класс Clients() из модуля Clients
Методы:

1. AddClient(FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class) - добавление нового клиента с указанными данными в журнал self.Log

2. AddClients(*lsts) - добавление нескольких работников. В качестве аргументов передаются списки содержащие необходимые данные в порядке ввода аргументов метода AddClient(FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class)

3. DelClient(FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class) - удаление клиента с указанными данными из журнала self.Log. Выводит предупреждение если журнал пуст или такого клиента не зарегистрировано

4. DelClients(*lsts) - удаление нескольких клиентов. В качестве аргументов передаются списки содержащие необходимые данные в порядке ввода аргументов метода DelClient(FirstName, LastName, Passport, EMail, PhoneNumber, HostCountry, HostCity, Class)

5. ViewLog - просмотр данных журнала в удобном для чтения формате

## Класс Deals() из модуля Deals

Методы:

1. addDeal(self, FirstName, LastName, Passport, Email, PhoneNumber, HostCountry, HostCity, Class) - добавление заказа тура в журнал self.Log. Выводит предупреждение если такого клиента не зарегистрировано

2. ViewLog - просмотр данных журнала в удобном для чтения формате

## Модуль main 

Создание объектов основных классов и работа с ними

В качестве примера работы с симулятором использованы основные методы классов Workers(), Clients(), Deals()

```html
<meta name="viewport" content="width=device-width, initial-scale=1.0">
```
