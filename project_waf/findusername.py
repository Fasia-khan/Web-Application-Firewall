import getpass
from typing import Optional, Any


def user():
    username: str = getpass.getuser()
    #print(username)
    return username
#user()