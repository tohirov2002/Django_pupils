from django.db import models

# Create your models here.


class Pupil(models.Model):
    name = models.CharField(max_length=50,verbose_name='Pupil name')
    age = models.IntegerField(verbose_name='Pupil age')
    mark_1 = models.IntegerField(verbose_name='First month')
    mark_2 = models.IntegerField(verbose_name='Second month')
    mark_3 = models.IntegerField(verbose_name='Third month')
    mark_4 = models.IntegerField(verbose_name='Fourth month')
    mark_5 = models.IntegerField(verbose_name='Fifth month')
    mark_6 = models.IntegerField(verbose_name='Sixth month')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'pupils'
        verbose_name = 'Pupils list'
        ordering = ('id',)



