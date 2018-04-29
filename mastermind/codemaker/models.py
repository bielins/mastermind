from django.db import models

# Create your models here.

class Game(models.Model):
    idGame = models.AutoField(primary_key=True)
    colorCode = models.CharField(max_length=4)

    def __str__(self):
        return str(self.idGame)