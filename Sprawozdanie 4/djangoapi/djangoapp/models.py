from django.db import models

class KartyGraficzne(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)

    def __str__(self):
        return self.name