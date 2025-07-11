import sys


def call_center(clients, recipients):
    return list(set(clients)-set(recipients))


def potential_clients(participants, clients):
    return list(set(participants)-set(clients))


def loyalty_program(clients, participants):
    return list(set(clients)-set(participants))


def business_task(command):
    clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com',
               'john@snow.is', 'bill_gates@live.com', 'mark@facebook.com',
               'elon@paypal.com', 'jessica@gmail.com']
    participants = ['walter@heisenberg.com', 'vasily@mail.ru',
                    'pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com',
                    'pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
    recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']

    if command == 'call_center':
        print(*call_center(clients, recipients), sep=', ')
    elif command == 'potential_clients':
        print(*potential_clients(participants, clients), sep=', ')
    elif command == 'loyalty_program':
        print(*loyalty_program(clients, participants), sep=', ')
    else:
        raise ValueError(
            'the argument should be one of the following: call_center, potential_clients,loyalty_program')


if __name__ == '__main__':

    if len(sys.argv) == 2:
        arg = sys.argv[1]
        try:
            business_task(arg)
        except ValueError as error:
            print(error)
    else:
        raise ValueError('wrong number of arguments')
