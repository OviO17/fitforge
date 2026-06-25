from django.db import models
from django.urls import reverse


class Product(models.Model):
    WORKOUT_PLAN = 'workout_plan'
    NUTRITION_PLAN = 'nutrition_plan'
    MERCHANDISE = 'merchandise'

    PRODUCT_TYPES = [
        (WORKOUT_PLAN, 'Workout plan'),
        (NUTRITION_PLAN, 'Nutrition plan'),
        (MERCHANDISE, 'Merchandise'),
    ]

    name = models.CharField(max_length=140)
    slug = models.SlugField(unique=True)
    product_type = models.CharField(max_length=30, choices=PRODUCT_TYPES)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    stock = models.PositiveIntegerField(default=20)
    is_active = models.BooleanField(default=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['product_type', 'name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'slug': self.slug})

    @property
    def is_in_stock(self):
        return self.stock > 0 or self.product_type != self.MERCHANDISE

# Create your models here.
