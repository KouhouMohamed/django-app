from django.db import models
import sqlite3


class StudentStage(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    school = models.CharField(max_length=1000)
    image = models.CharField(max_length=1000)

    class Meta:
        unique_together = ('name','school','image')

    def __str__(self):
        return self.name


