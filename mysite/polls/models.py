from django.db import models

# Create your models here.
class Date(models.Model):
   date_year = models.CharField(max_length=4)
   date_month = models.CharField(max_length=2)
   date_day = models.CharField(max_length=2)

   def __str__(self):
     return self.date_year

class Post(models.Model):
  post_title = models.CharField(max_length=50)
  post_text = models.CharField(max_length=400)
  pub_time = models.DateTimeField('date published')
  date_id = models.ForeignKey('Date', on_delete=models.CASCADE, null=True)

  def __str__(self):
    return self.post_title
