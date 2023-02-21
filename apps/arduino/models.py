from django.db import models

class HeartRateData(models.Model):
    beat = models.IntegerField()

    def __str__(self):
        return str(self.beat)