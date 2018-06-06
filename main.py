# Условиие:
# Создать программу, которая будет симулировать работу туроператора.
# Должны присутствовать классы сотрудников, клиентов, туров, совершенных сделок и т.д.
# Программа должна выводить историю совершенных покупок клиентом, продаж одного сотрудника,
# количество продаж по дням, туры в определенный срок и т.д.(доп. функционал можете продумать сами)
# Я, как клиент, могу зарегистрироваться (т.е. создать объект имени меня) и "купить" тур


# Примечание:
# 1. В задаче рассмотрены только клиенты без детей и жены/мужа
#    При необходимости код может быть обновлен с учетом этих условий
# 2. В задаче рассмотрены постоянные константы для рассчета стоимости тура
#    При необходимости код может быть обновлен с учетом определенных коэффициентов для разных стран и иных условий

import Workers, Clients, Deals

wrks = Workers.Workers()
clts = Clients.Clients()
dls = Deals.Deals()
if __name__ == '__main__':
    print('\033[1mWelcome to the tour operator simulator\033[0m')


    def program():
        command = input('Which command you want to choose:\n'
                        '\t1. Add of worker\n'
                        '\t2. Add of workers\n'
                        '\t3. Delete of worker\n'
                        '\t4. Delete of workers\n'
                        '\t5. View of log of workers\n'
                        '\t6. Add of client\n'
                        '\t7. Add of clients\n'
                        '\t8. Delete of client\n'
                        '\t9. Delete of clients\n'
                        '\t10. View of log of clients\n'
                        '\t11. Add of deal\n'
                        '\t12. View of log of deals\n'
                        '\t13. Exit from program\n'
                        'Enter the number or name of the command.\n')

        if command == '1' or command == 'Add of worker':
            data = input('Enter a space separated first name, last name, sex, position and department of work.\n').split()
            try:
                wrks.AddWorker(*data)
            except TypeError:
                print('Data entered incorrectly')
            return program()

        elif command == '2' or command == 'Add of workers':
            data = input('Enter the first name, last name, sex, '
                         'position and department of work of several workers through a space in turn.\n').split()
            try:
                for i in zip(*[iter(data)] * 5):
                    wrks.AddWorker(*i)
            except TypeError:
                print('Data entered incorrectly')
            return program()

        elif command == '3' or command == 'Delete of worker':
            data = input('Enter a space separated first name, last name, sex, position and department of work.\n').split()
            try:
                wrks.DelWorker(*data)
            except TypeError:
                print('Data entered incorrectly')
            return program()

        elif command == '4' or command == 'Delete of workers':
            data = input('Enter the first name, last name, sex, '
                         'position and department of work of several workers through a space in turn.\n').split()
            try:
                for i in zip([*iter(data)] * 5):
                    wrks.DelWorker(*i)
            except TypeError:
                print('Data entered incorrectly')
            return program()

        elif command == '5' or command == 'View of log of workers':
            wrks.ViewLog
            return program()

        elif command == '6' or command == 'Add of client':
            data = input('Enter a space separated first name, last name, passport number, email, phone number, host country, '
                         'host city and flight class of client.\n').split()
            try:
                clts.AddClient(*data)
            except TypeError:
                print('Data entered incorrectly')
            return program()

        elif command == '7' or command == 'Add of clients':
            data = input('Enter a space through the first name, last name, passport number, email, phone number, host country, '
                         'host city and flight class of several customers through a space in turn.\n').split()
            try:
                for i in zip(*[iter(data)] * 8):
                    clts.AddClient(*i)
            except TypeError:
                print('Data entered incorrectly')
            return program()

        elif command == '8' or command == 'Delete of client':
            data = input('Enter a space separated first name, last name, passport number, email, phone number, host country, '
                         'host city and flight class of client.\n').split()
            try:
                clts.DelClient(*data)
            except TypeError:
                print('Data entered incorrectly')
            return program()

        elif command == '9' or command == 'Delete of clients':
            data = input('Enter a space through the first name, last name, passport number, email, phone number, host country, '
                         'host city and flight class of several customers through a space in turn.\n').split()
            try:
                for i in zip(*[iter(data)] * 8):
                    clts.DelClient(*i)
            except TypeError:
                print('Data entered incorrectly')
            return program()

        elif command == '10' or command == 'View of log of clients':
            clts.ViewLog
            return program()

        elif command == '11' or command == 'Add of deal':
            data = input('Enter a space separated first name, last name, passport number, email, phone number, host country, '
                         'host city and flight class of client.\n').split()
            try:
                dls.addDeal(*data)
            except TypeError:
                print('Data entered incorrectly')
            return program()

        elif command == '12' or command == 'View of log of deals':
            dls.ViewLog
            return program()

        elif command == '13' or command == 'Exit from program':
            print('Work with the program is completed')

        else:
            print('The entered command was not found, try again')
            return program()


    program()

# if __name__ == '__main__':
#     # Пример работы с классом Workers.Workers() в коде
#     workers = [['John', 'Snow', 'Male', 'Operator', 'Call Center'],
#                ['Harry', 'Potter', 'Male', 'Manager', 'Management'],
#                ['Mary', 'Jane', 'Female', 'Operator', 'Call Center'],
#                ['Barry', 'Allen', 'Male', 'Operator', 'Call Center']] John Snow Male Operator Call-Center Barry Allen Male Operator Call-Center
#     for i in workers:
#         wrks.AddWorker(*i)
#     wrks.DelWorker('John', 'Snow', 'Male', 'Operator', 'Call Center')
#     wrks.ViewLog
#
#     # Пример работы с классом Clients.Clients() в коде
#     clients = [['Anar', 'Dadashov', '9898111222', 'anardadashov00@gmail.com', '8-909-970-05-32', 'Italy', 'Rome', 'First Class'],
#                ['Harry', 'Potter', '1234567890', 'harrypotter@hogwarts.magic', '8-11-787-87-87', 'England', 'London', 'Business Class'],
#                ['Mary', 'Jane', '1010987456', 'maryjane@spider.man', '8-917-120-17-28', 'Japan', 'Tokyo', 'Economy Class'],
#                ['Barry', 'Allen', '1223334444', 'barryallen@speed.force', '8-159-012-57-99', 'Future', 'Flash Point', 'First Class']]
#
#     for i in clients:
#         clts.AddClient(*i)
#
#     clts.DelClient('Anar', 'Dadashov', '9898111222', 'anardadashov00@gmail.com', '8-909-970-05-32', 'Italy', 'Rome', 'First Class')
#     clts.ViewLog
#
#     # Пример работы с классом Deals.Deals() в коде
#     dls.addDeal('Harry', 'Potter', '1234567890', 'harrypotter@hogwarts.magic', '8-11-787-87-87', 'England', 'London', 'Business Class')
#     dls.addDeal('Barry', 'Allen', '1223334444', 'barryallen@speed.force', '8-159-012-57-99', 'Future', 'Flash Point', 'First Class')
#     dls.addDeal('Friedrich', 'Nietzsche', '4564567895', 'qweuywwihw@skdnfs.fjd', '8-000-001-01-10', 'Afterlife', 'Paradise', 'First Class')
#     dls.ViewLog
