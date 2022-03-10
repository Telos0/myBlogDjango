from django.db import models

# Create your models here.

class Contents(models.Model):
    contentsid = models.CharField(max_length=30)
    content = models.TextField(null=True)
    order = models.IntegerField()
    useYN = models.BooleanField(default='Y')

    def __str__(self):
        return f'{self.contentsid} : {self.order} : {self.useYN}'