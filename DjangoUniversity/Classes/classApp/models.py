from django.db import models

# Created a model.

class djangoClasses(models.Model):
    Title = models.CharField(max_length=50)
    Course = models.IntegerField()
    Instructor_Name = models.CharField(max_length=30)
    Duration = models.FloatField()

# Added three objects from the class with attribute values
course1 = djangoClasses("Underwater Basket Weaving", 101, "Alice Apple", 1.5 )

course2 = djangoClasses("Python Problems", 102, "Bob Banana", 2.0)

course3 = djangoClasses("SQL School", 103, "Carey Cabbage", 1.75)
