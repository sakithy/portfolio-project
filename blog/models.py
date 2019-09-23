from django.db import models

# Create your models here.
# title
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

# pub_date
# body
# image


# Add the blog app to the setting

# create a migration

# Migrate

# Add to the Admin
