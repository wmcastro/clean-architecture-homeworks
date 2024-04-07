from connection.my_sql_repository import MySQLRepository
from entities.user import User

class UserService:
    def get_entity(self):
        print('Getting User table...')
        entity_object = MySQLRepository().get_session(User())
        print('Results about User table', entity_object)
        return entity_object