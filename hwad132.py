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
            self.starred_rus = 'да'
        elif self.starred == False:
            self.starred_rus = 'нет'

        self.str_args = str()
        for arg in self.args:
            self.str_args += ('       ' + str(arg) + '\n')

        self.str_kwargs = str()
        for key in self.kwargs:
            self.str_kwargs += ('       '+f'{key}: {self.kwargs[key]}' + '\n')

        return f'Имя: {self.firstname}\n' \
               f'Фамилия: {self.lastname}\n' \
               f'Телефон: {self.number}\n' \
               f'В избранных: {self.starred_rus}\n' \
               f'Дополнительная информация: \n' \
               f'{self.str_args}' \
               f'{self.str_kwargs}'


class Phonebook:

    def __init__(self):
        contact = Contact()
        self.contacts = {contact.number: contact}

    def add_contact(self, contact, *args, **kwargs):
        contact.firstname = input('Введите имя контакта')
        contact.lastname = input('Введите фамилию')
        contact.number = input('Введите номер телефона')
        starred_input = input('Добавить контакт в избранные? (да/нет)')
        if starred_input == 'да':
            contact.starred = 'True'
        elif starred_input == 'нет':
            contact.starred = 'False'
        contact.args = input('Введите дополнительную информацию о контакте (через запятую): ')
        while input('Добавить соцсеть? (да/нет)') == 'да':
            contact.kwargs = dict()
            kwargs_input = input('Введите название и адрес соцсети через запятую: ')
            contact.kwargs.key = kwargs_input[0]
            contact.kwargs.value = kwargs_input[1]

        self.contacts.update(contact.number, contact)

phonebook = Phonebook()
phonebook.add_contact()
