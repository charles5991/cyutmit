from django.db import models



class Introduction(models.Model):
    title = models.TextField()
    content = models.TextField(default='')

    def __str__(self):
        return self.title
