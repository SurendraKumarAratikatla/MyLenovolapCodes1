from django.db import models

class game(models.Model):
    player1 = models.CharField(max_length=100)
    player2 = models.CharField(max_length=100)
    player3 = models.CharField(max_length=100)
    player4 = models.CharField(max_length=100)

    def __str__(self):
        return self.player1
