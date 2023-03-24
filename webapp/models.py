from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe
class Car(models.Model):
    """Car Model"""

    TRANSMISSION_CHOICES = [
        ('automatic', 'Automatic'),
        ('manual', 'Manual'),
    ]

    title = models.CharField(max_length=100)
    door_num = models.PositiveIntegerField()
    seat_num = models.PositiveIntegerField()
    transmission = models.CharField(max_length=10, choices=TRANSMISSION_CHOICES)
    rating = models.IntegerField(validators=[
        MinValueValidator(0),
        MaxValueValidator(5)
    ])
    price = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='car_photos/', blank=True)
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('webapp:car_detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural = "Cars"

    @property
    def photo_url(self):
        return self.photo.url if self.photo else ''

    def image_tag(self):
        return mark_safe('<img src="%s" width="150" height="150" />' % self.photo.url)

    image_tag.short_description = 'Image'


