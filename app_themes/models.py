from django.db import models

# Create your models here.


class Themes(models.Model):
    name = models.CharField(max_length=50,verbose_name='Themes name')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'themes'
        verbose_name = 'Themes list'
        # ordering = ('id',)