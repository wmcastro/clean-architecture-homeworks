from services.user_service import UserService

def execute_user():
    result =  UserService().get_entity()
    print(result)

execute_user()