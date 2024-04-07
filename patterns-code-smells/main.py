from controllers.controller import controller
from services.user_service import UserService

# Here, the controller calls the view and returns the User's information.
@controller
def execute_user():
    result = UserService().get_entity()
    print(result)

# Now, the method is called manually but in a Backend, here an endpoint would be invoked.
execute_user()