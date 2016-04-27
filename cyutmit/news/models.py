from django.db import models



class News(models.Model):
    title = models.TextField()
    content = models.TextField(default='')
    postTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-postTime', )