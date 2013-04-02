from django.db import models

class Gossip(models.Model):
    title = models.TextField()
    body = models.TextField()
    date = models.DateTimeField()
    priority = models.SmallIntegerField(default=0)

    def __unicode__(self):
        return self.title

class Destination(models.Model):
    name = models.TextField()
    slug = models.SlugField()
    iso3 = models.CharField(max_length=3)

    def __unicode__(self):
        return self.name

class Photo(models.Model):
    caption = models.TextField()
    fn = models.CharField(max_length=30)
    destination = models.ForeignKey('Destination')
    deleted = models.SmallIntegerField()
    orientation = models.CharField(max_length=30)

    def __unicode__(self):
        return self.fn
