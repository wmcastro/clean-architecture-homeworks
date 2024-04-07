# TODO FIX THIS
class DBRepository:
    def __init__(self) -> None:
        mysql_db_connection_string = 'mysql://username:password@localhost/database_name'
        self.engine = ''
        print('Creating engine and session at your', mysql_db_connection_string)
    
    def connect_to_db(self):
        print('Connecting to yourDB...')
        print('Connected to DB...')
        return 'Information of entity'

    def get_session(self):
        return self.connect_to_db

    def close_connection(self):
        print('DB closed. Bye!')