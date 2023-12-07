from django.db import models

# Create your models here.


class UserPost(models.Model):
    user_id = models.IntegerField(unique=True)
    post_id = models.AutoField(primary_key=True)
    content = models.CharField(max_length=500, null=True)
    words_count = models.IntegerField(default=0)
    words_average_length = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)


    #"my name is gaurav. I am 10 years old"

