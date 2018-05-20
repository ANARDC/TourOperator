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
    # Работа с классом Workers.Workers()
    workers = [['John', 'Snow', 'Male', 'Operator', 'Call Center'],
               ['Harry', 'Potter', 'Male', 'Manager', 'Management'],
               ['Mary', 'Jane', 'Female', 'Operator', 'Call Center'],
               ['Barry', 'Allen', 'Male', 'Operator', 'Call Center']]
    for i in workers:
        wrks.AddWorker(*i)
    wrks.DelWorker('John', 'Snow', 'Male', 'Operator', 'Call Center')
    wrks.ViewLog

    # Работа с классом Clients.Clients()
    clients = [['Anar', 'Dadashov', '9898111222', 'anardadashov00@gmail.com', '8-909-970-05-32', 'Italy', 'Rome', 'First Class'],
               ['Harry', 'Potter', '1234567890', 'harrypotter@hogwarts.magic', '8-11-787-87-87', 'England', 'London', 'Business Class'],
               ['Mary', 'Jane', '1010987456', 'maryjane@spider.man', '8-917-120-17-28', 'Japan', 'Tokyo', 'Economy Class'],
               ['Barry', 'Allen', '1223334444', 'barryallen@speed.force', '8-159-012-57-99', 'Future', 'Flash Point', 'First Class']]

    for i in clients:
        clts.AddClient(*i)

    clts.DelClient('Anar', 'Dadashov', '9898111222', 'anardadashov00@gmail.com', '8-909-970-05-32', 'Italy', 'Rome', 'First Class')
    clts.ViewLog

    # Работа с классом Deals.Deals()
    dls.addDeal('Harry', 'Potter', '1234567890', 'harrypotter@hogwarts.magic', '8-11-787-87-87', 'England', 'London', 'Business Class')
    dls.addDeal('Barry', 'Allen', '1223334444', 'barryallen@speed.force', '8-159-012-57-99', 'Future', 'Flash Point', 'First Class')
    dls.addDeal('Friedrich', 'Nietzsche', '4564567895', 'qweuywwihw@skdnfs.fjd', '8-000-001-01-10', 'Afterlife', 'Paradise', 'First Class')
    dls.ViewLog