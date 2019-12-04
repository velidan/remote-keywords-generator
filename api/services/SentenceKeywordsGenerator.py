"""
Use this service to genenerate keywords combinations
based on a sentence. You should pass the sentence
that you want to generate keywords for
"""
from itertools import combinations
import re

def getKeywordsForSentence(sentence):
    # keywords result
    keywords_list = []

    # removing special chars
    sentence_sanitized = re.sub(r'\W', ' ', sentence)
    
    sentence_words_list = sentence_sanitized.split()
    
    # generating possible keywords combinations based on the title
    for i in range(len(sentence_words_list), 0, -1):
        for group in combinations(sentence_words_list, i):
            keywords_list.append(' '.join(group))

    return keywords_list