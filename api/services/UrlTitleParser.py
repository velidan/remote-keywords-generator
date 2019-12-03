"""
Use this service to parse a passed url and get a title of it
"""

import certifi
import urllib3
from bs4 import BeautifulSoup

class UrlDoesntExists(Exception):
    """ Raises when the program can't connect to the passed URL """

    def __str__(self):
        return 'The passed URL is does not exist'

def getPageTitleByUrl(url):
    # adding ssl certificates
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                                ca_certs=certifi.where())

    # check if the URL exists by a simple HEAD request
    try:
        head_response = http.request('HEAD', url)

    except urllib3.exceptions.MaxRetryError as e:
        raise UrlDoesntExists()

    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, 'html.parser')
    return soup.title.string