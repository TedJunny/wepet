from django.db import models


class Dog(models.Model):
    name = models.CharField(max_length=45)
    age = models.PositiveSmallIntegerField()
    owner = models.ForeignKey("owners.Owner", on_delete=models.CASCADE)

    class Meta:
        db_table = "dogs"
