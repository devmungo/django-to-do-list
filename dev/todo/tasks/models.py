from django.db import models

# Create your models here.
class Task(models.Model): #Inherit the Model class which gives us the ability to our own custom djagno model
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title #this is so we can see the title of the task in the admin panel
