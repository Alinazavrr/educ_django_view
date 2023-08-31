from django.db import models

# Create your models here.


class Application(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    question = models.TextField()
    manager_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} / {self.name} / {self.manager_id}'
