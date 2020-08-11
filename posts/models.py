from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    post_image = models.ImageField(upload_to='assets/img/posts')
    pub_date = models.DateField('Date Published',default=timezone.now)

    def __str__(self):
        return self.title