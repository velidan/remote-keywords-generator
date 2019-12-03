"""
Use this service to genenerate keywords combinations
based on a title of the remote webpage. You should pass the URL
of the webpage that you want to generate keywords for
"""
from itertools import combinations
import re

from bs4 import BeautifulSoup

from .UrlTitleParser import getPageTitleByUrl

def getKeywordsForUrl(url):
    # keywords result
    keywords_list = []

    title = getPageTitleByUrl(url)
    
    # removing special chars
    title_sanitized = re.sub(r'\W', ' ', title)
    
    title_words_list = title_sanitized.split()
    
    # generating possible keywords combinations based on the title
    for i in range(len(title_words_list), 0, -1):
        for group in combinations(title_words_list, i):
            keywords_list.append(' '.join(group))

    return keywords_list