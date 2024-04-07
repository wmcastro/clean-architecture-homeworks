from interfaces.entities import InterfaceEntity

class User(InterfaceEntity):
    def __init__(self):
        print('Info about your entity:')
        id = 'id'
        name = 'Name'
        age = 'age'
        email = 'email'
        country = 'country'