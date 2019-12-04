"""
Use this service to parse a passed url and get a title of it
"""

# uncomment to log the request headers
# import http.client
# http.client.HTTPConnection.debuglevel = 5

import certifi
import urllib3
from bs4 import BeautifulSoup

from api.errors.UrlDoesntExist import UrlDoesntExist
from api.services.UserAgent import getRandomAgent

default_headers = {
    'User-Agent': getRandomAgent()
}

def getPageTitleByUrl(url):
    # adding ssl certificates
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED',
                                ca_certs=certifi.where())

    # check if the URL exists by a simple HEAD request
    try:
        http.request('HEAD', url, headers=default_headers)

    except urllib3.exceptions.MaxRetryError as e:
        raise UrlDoesntExist()

    response = http.request('GET', url, headers=default_headers)
    soup = BeautifulSoup(response.data, 'html.parser')
    return soup.title.string

