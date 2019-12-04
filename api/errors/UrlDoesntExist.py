
"""
A custom error when the passed url doesn't exist
"""
class UrlDoesntExist(Exception):
    """ Raises when the program can't connect to the passed URL """

    def __str__(self):
        return 'The passed URL is does not exist'
