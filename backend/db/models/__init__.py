### file to avoid error: sqlalchemy.exc.InvalidRequestError: When initializing mapper Mapper[User(users)], expression 'UserInQueue' failed to locate a name ('UserInQueue'). If this is a class name, consider adding this relationship() to the <class 'db.models.user.User'> class after both dependent classes have been defined.
from db.models.queue import Queue
from db.models.user import User
from db.models.user_in_queue import UserInQueue
