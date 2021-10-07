def greeting():
    print('Hello world')


def greeting(name):
    print('Hello', name)


greeting('Erin')
greeting('Paolo')
greeting('Tanya')


def about_me(fave_food, fave_animal, fave_place):
    print('I love to eat', fave_food, 'while petting my',
          fave_animal, 'at', fave_place)


about_me('sushi', 'cat', 'the beach')

about_me('the beach', 'sushi', 'cat')

about_me(fave_place='the beach', fave_food='sushi', fave_animal='cat')


def accept_phone(number, phone_type):
    print('The phone number', number, 'is a', phone_type, 'phone')


accept_phone('555-1234', 'home')
accept_phone('555-5678', 'cell')
accept_phone('555-8765', 'work')


def accept_phone(number, phone_type='cell'):
    print('The phone number', number, 'is a', phone_type, 'phone')


def greeting():
    print('Hello', name)


name = 'Marco'
greeting()


def greeting():
    name = 'Maria'
    print('Hello', name)


name = 'Marco'
greeting()


def greeting():
    global name
    print('Hello', name)
    name = 'Maria'
    print('Hello', name)


name = "Marco"
greeting()
