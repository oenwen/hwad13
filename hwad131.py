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

if __name__ == '__main__':

    contact = Contact('John', 'Smith', '9999999999', True, '123456', '456789', telegram = '@johny', email = 'johny@smith.com')
    print(contact)

