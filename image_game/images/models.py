from django.db import models


class Image(models.Model):
    def __str__(self):
        return str(list(self.tag_set.all()[:5]))

    url = models.CharField(max_length=255)


class Tag(models.Model):
    def __str__(self):
        return '{}'.format(self.description)

    def __repr__(self):
        return '{}'.format(self.description)

    description = models.CharField(max_length=255)
    confidence = models.FloatField(null=True)
    score = models.FloatField()
    mid = models.CharField(max_length=255)

    image = models.ForeignKey(Image, on_delete=models.CASCADE)
