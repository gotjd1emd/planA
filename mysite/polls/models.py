from django.db import models

# Create your models here.
class Posts(models.Model):
  post_title = models.CharField(max_length=50)
  post_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  def __str__(self):
    return self.post_title
