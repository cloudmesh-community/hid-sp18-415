
import connexion
import six

from swagger_server.models.user_identity import UserIdentity  # noqa: E501
from swagger_server import util


def get_user_identity(ID, username):  # noqa: E501
    """User identification

    Return user identity # noqa: E501

    :param ID: user id
    :type ID: int
    :param username: username
    :type username: str

    :rtype: UserIdentity
    """
    for username in UserIdentity:
       if username = "True" and id = "True":
          return username.id
       elif id = "False":
          return "invalid id"

    return Identity(get_user_identity())
