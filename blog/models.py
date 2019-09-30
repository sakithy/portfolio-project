from django.db import models
import time

# Create your models here.
# title
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def date(self):
        return self.pub_date.strftime('%b %e %Y')
# pub_date
# body
# image


# Add the blog app to the setting

# create a migration

# Migrate

# Add to the Admin
