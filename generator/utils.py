import string

from random import choices


def generate_a_short_url(size):
    """
    Generate a short url version for a specific url with the passed size.
    """
    return ''.join(choices(string.ascii_letters + string.digits, k=size))
