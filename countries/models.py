from django.db import models

class ActiveManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(active=True)


class Country(models.Model):
    CODES_CHOICES =(
        ('CO', 'colombia'),
        ('MX', 'mexico' ),
        ('USA', 'Estados Unidos'),
        ('AR', 'argentina'),
    )

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3, choices=CODES_CHOICES)
    continent = models.ForeignKey('continents.Continent', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    active_manager = ActiveManager()

    def __str__(self):
        return self.name
