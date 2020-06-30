from django.db import models

# Create your models here.
class Todo(models.Model):
    todo = models.CharField(max_length=100, null=False,
                            help_text="")
    done = models.BooleanField(default=False)
    def __str__(self):
      return self.todo