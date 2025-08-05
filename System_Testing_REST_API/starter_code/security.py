from models.user import UserModel
from werkzeug.security import check_password_hash

def authenticate(username,password):
    """
    Function that gets called when a user calls the /auth endpoint
    with their username and password.
    :param username: User's username in string format.
    :param password: User's un-encrypted password in string format.
    :return: A userModel object if authentication was successful, None otherwise.
    """
    user = UserModel.find_by_username(username)

    if user and user.check_password(password):
        return user
    if user and check_password_hash(user.password,password):
        return user
    return None

def identity(payload):
    """
    Function that gets called when user has already authenticated, and Flask-JWT
    verified their authorization header is correct.
    :param payload: A dictionary with 'identity' key, which is the user id.
    :return:A UserModel object.
    """
    user_id = int(payload['identity'])
    return UserModel.find_by_id(user_id)

