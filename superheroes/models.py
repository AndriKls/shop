from django.db import models

# Create your models here.

class Superhero(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nimi')
    civillian_name = models.CharField(max_length=100, verbose_name='Kodanikunimi')
    age = models.IntegerField(verbose_name='Vanus')
    location = models.CharField(max_length=100, verbose_name='Asukoht')
    description = models.TextField(blank=True, null=True, verbose_name="Kirjeldus")
    image = models.ImageField(upload_to='superheroes', blank=True, null=True, verbose_name='Pilt')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Superheroes'
        ordering = ['name']

    