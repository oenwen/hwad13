class


def add_contact(self, firstname, lastname, number, starred=False, *args, **kwargs):
    self.firstname = input('Введите имя контакта')
    self.lastname = input('Введите фамилию')
    self.number = input('Введите номер телефона')
    starred_input = input('Добавить контакт в избранные? (да/нет)')
    if starred_input == 'да':
        self.starred = 'True'
    elif starred_input == 'нет':
        self.starred = 'False'
    self.args = input('Введите дополнительную информацию о контакте (через запятую): ')
    while input('Добавить соцсеть? (да/нет)') == 'да':
        self.kwargs = dict()
        kwargs_input = input('Введите название и адрес соцсети через запятую: ')
        self.kwargs.key = kwargs_input[0]
        self.kwargs.value = kwargs_input[1]