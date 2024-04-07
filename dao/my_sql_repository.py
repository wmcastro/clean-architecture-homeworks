import time
from interfaces.dao import InterfaceDAO

class MySQLRepository(InterfaceDAO):
    def __init__(self) -> None:
        mysql_db_connection_string = 'mysql://username:password@localhost/database_name'
        self.engine = ''
        print('Creating engine and session at your', mysql_db_connection_string)

    def get_session(self, entity):
        print('Connecting to yourDB...')
        time.sleep(0.5)
        print('Connected to DB...')
        time.sleep(0.3)
        return entity

    def close_connection(self):
        print('DB closed. Bye!')