from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User as user
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length = 10)
    about = models.TextField()
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank = True, null = True)

class post(models.Model):
    post_id = models.IntegerField(primary_key = True)
    title = models.CharField(max_length = 10)
    image = models.ImageField()
    txt = models.TextField()
    created_date = models.DateTimeField()
    is_published = models.BooleanField()
    update = models.DateTimeField(blank = True , null = True)
    post_category = models.ForeignKey(category , on_delete = models.CASCADE)
    creator = models.ForeignKey(user , on_delete = models.CASCADE)

    def like_number(self):
        return self.like.count()
    
    def __str__(self):
        return self.title

class comment(models.Model):
    post_id = models.ForeignKey(post , on_delete = models.CASCADE)
    user_id = models.ForeignKey(user , on_delete = models.CASCADE)
    txt = models.TextField()
    send_date = models.DateTimeField()
    stars = models.PositiveSmallIntegerField()
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank = True, null = True)
    reply_txt = models.TextField(blank = True , null = True)

    def clean(self):
        if self.stars < 1 or self.stars > 5:
            raise ValidationError('Stars must be between 1 and 5')

class like(models.Model):
    post_id = models.ForeignKey(post , on_delete = models.CASCADE)
    user_id = models.ForeignKey(user , on_delete = models.CASCADE)

class save(models.Model):
    post_id = models.ForeignKey(post , on_delete = models.CASCADE)
    user_id = models.ForeignKey(user , on_delete = models.CASCADE)