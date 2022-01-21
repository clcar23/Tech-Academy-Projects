from django.db import models

# Created a model.

class djangoClasses(models.Model):
    Title = models.CharField(max_length=50)
    Course = models.IntegerField()
    Instructor_Name = models.CharField(max_length=30)
    Duration = models.FloatField()

    objects = models.Manager()

    def __str__(self):
        return self.name