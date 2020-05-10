class Contact:

    def __init__(self, firstname, lastname, number, starred = False, *args, **kwargs):
        self.firstname = firstname
        self.lastname = lastname
        self.number = number
        self.starred = starred
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        if self.starred == True:
            starred_rus = 'да'
        elif self.starred == False:
            starred_rus = 'нет'

        self.str_args = str()
        for arg in self.args:
            self.str_args += ('       ' + str(arg) + '\n')

        self.str_kwargs = str()
        for key in self.kwargs:
            self.str_kwargs += ('       '+f'{key}: {self.kwargs[key]}' + '\n')

        return f'Имя: {self.firstname}\n' \
               f'Фамилия: {self.lastname}\n' \
               f'Телефон: {self.number}\n' \
               f'В избранных: {starred_rus}\n' \
               f'Дополнительная информация: \n' \
               f'{self.str_args}' \
               f'{self.str_kwargs}'


class Phonebook:

    def __init__(self):
        self.contact = Contact('', '', '')
        self.contacts = {self.contact.number: self.contact}


    def add_contacts(self, *args, **kwargs):
        while True:
            user_input = input('Добавить новый контакт (да/нет)? ')
            if user_input == 'нет':
                break
            elif user_input == 'да':
                firstname = input('Введите имя контакта ')
                lastname = input('Введите фамилию ')
                number = input('Введите номер телефона ')
                starred_rus = input('Добавить контакт в избранные? (да/нет) ')
                if starred_rus == 'да':
                    starred = True
                elif starred_rus == 'нет':
                    starred = False
                args_list = []
                while True:
                    arg = input('Введите дополнительную информацию о контакте или введите "-", чтобы пропустить ввод: ')
                    if arg == '-':
                        break
                    else:
                        args_list.append(arg)
                args = tuple(args_list)
                while input('Добавить соцсеть? (да/нет) ') == 'да':
                    kwargs = dict()
                    kwargs_key = input('Введите название соцсети: ')
                    kwargs_value = input('Введите адрес соцсети: ')
                    kwargs.update({kwargs_key: kwargs_value})

                self.contact = Contact(firstname, lastname, number, starred, *args, **kwargs)
            self.contacts.update({self.contact.number: self.contact})


if __name__ == '__main__':
    phonebook = Phonebook()
    while True:
        func = input('Введите команду:\n'
                     'a - добавить контакт(ы)\n'
                     'p - печать телефонной книги\n'
                     'q - выход\n'
                     '')
        if func == 'q':
            break
        elif func == 'a':
            phonebook.add_contacts()
        elif func == 'p':
            for contact in phonebook.contacts.values():
                print(contact)