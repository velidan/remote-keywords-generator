"""
A URL model that contains it's address, keywords and creation time
"""

from django.db import models
import json

class Url(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    title = models.TextField(default=None)
    keywords = models.TextField(default=None)

    def set_keywords(self, data):
        self.keywords = json.dumps(data)

    def get_keywords(self):
        return json.loads(self.keywords)

    def __str__(self):
        return '''url: {0},
                  title: {1},
                  keywords: {2}'''.format(self.address,
                                           self.title,
                                           self.keywords)