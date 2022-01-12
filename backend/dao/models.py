from django.db import models

# Create your models here.
class NftProject(models.Model):
    name = models.CharField(max_length=200)
    mainImage = models.ImageField(null=True, blank=True)
    twitterLink = models.URLField(null=True, blank=True)
    discordLink = models.URLField(null=True, blank=True)
    homepageLink = models.URLField(null=True, blank=True)
    plusLink1 = models.URLField(null=True, blank=True)
    plusLink2 = models.URLField(null=True, blank=True)
    create_date = models.DateTimeField()

    def __str__(self):
        return self.name