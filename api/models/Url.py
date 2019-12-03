from django.db import models
import json

class Url(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    address = models.TextField()
    keywords = models.TextField()

    def set_keywords(self, data):
        # convert a string list to string to save in db
        keywords_str = ', '.join(data)
        self.keywords = json.dumps(keywords_str)

    def get_keywords(self):
        return json.loads(self.keywords)

    def __str__(self):
        return 'url: {0}, keywords: {1}'.format(self.address, self.keywords)