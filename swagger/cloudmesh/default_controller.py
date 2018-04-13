import connexion
import six

from swagger_server.models.user_identity import UserIdentity  # noqa: E501
from swagger_server import util


def identity_get(ID, username):  # noqa: E501
    """User identification

    Return user identity # noqa: E501

    :param ID: user id
    :type ID: int
    :param username: username
    :type username: str

    :rtype: UserIdentity
    """
      
    return Identity(get_user_identity())
