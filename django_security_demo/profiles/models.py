from django.db import models


class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to='profiles/pictures', blank=True)
    description = models.TextField()
    website = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = 'user profile'
        verbose_name_plural = 'users profiles'

    def __unicode__(self):
        return self.name

