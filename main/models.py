from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class BaseModel(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        abstract = True


class TagsCategory(BaseModel):
    pass

    def __str__(self):
        return self.title


class Tag(BaseModel):
    category = models.ForeignKey(TagsCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Category(BaseModel):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Product(BaseModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    tags = models.ManyToManyField(Tag)
    unit_price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.title