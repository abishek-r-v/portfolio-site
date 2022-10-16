from django.db import models


# Create your models here
class AboutMeContent(models.Model):
    class Meta:
        db_table = 'about_me_content'

    paragraph_id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=1200)

    def __str__(self):
        return self.description[:20] + '...'


