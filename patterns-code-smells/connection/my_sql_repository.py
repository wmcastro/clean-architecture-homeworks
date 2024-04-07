class MySQLRepository:
    def __init__(self) -> None:
        mysql_db_connection_string = 'mysql://username:password@localhost/database_name'
        self.engine = ''
        print('Creating engine and session at your', mysql_db_connection_string)

    def get_session(self, entity):
        print('Connecting to yourDB...')
        print('Connected to DB...')
        return 'Information of entity'

    def close_connection(self):
        print('DB closed. Bye!')