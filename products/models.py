from django.db import models

from general.models import BaseModel
from products.validators import validator_rating


class Category(BaseModel):
	title = models.CharField(max_length=31)


class Brand(BaseModel):
	title = models.CharField(max_length=31)


class Size(BaseModel):
	title = models.CharField(max_length=31)


class Color(BaseModel):
	title = models.CharField(max_length=31)
	code = models.CharField(max_length=21)


class Tags(BaseModel):
	title = models.CharField(max_length=31)


class Product(BaseModel):
	title = models.CharField(max_length=31)
	description = models.TextField()
	price = models.FloatField()
	photo = models.ImageField(upload_to='products/images')
	color = models.ForeignKey(Color, on_delete=models.CASCADE)
	rating = models.PositiveIntegerField(validators=[validator_rating])
