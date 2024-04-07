from dao.my_sql_repository import MySQLRepository
from entities.user import User

from interfaces.services import InterfaceService

class UserService(InterfaceService):
    def get_entity(self):
        entity_object = MySQLRepository().get_session(User())
        print('Results about User table')
        return entity_object