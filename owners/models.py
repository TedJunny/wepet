from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField()
    age = models.PositiveSmallIntegerField()

    class Meta:
        db_table = "owners"
