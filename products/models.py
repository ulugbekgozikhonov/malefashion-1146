from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.db import models
from django.utils import timezone

from general.models import BaseModel
from products.validators import validator_rating


class Category(BaseModel):
	title = models.CharField(max_length=31)

	def __str__(self):
		return self.title


class Brand(BaseModel):
	title = models.CharField(max_length=31)

	def __str__(self):
		return self.title


class Size(BaseModel):
	title = models.CharField(max_length=31)

	def __str__(self):
		return self.title


class Color(BaseModel):
	title = models.CharField(max_length=31)
	code = models.CharField(max_length=21)

	def __str__(self):
		return self.title


class Tags(BaseModel):
	title = models.CharField(max_length=31)

	def __str__(self):
		return self.title


class Product(BaseModel):
	name = models.CharField(max_length=31)
	description = models.TextField()
	price = models.FloatField()
	discount = models.FloatField()
	photo = models.ImageField(upload_to='products/images')
	rating = models.PositiveIntegerField(default=1, validators=[validator_rating])
	category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
	brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name="products")
	size = models.ManyToManyField(Size, blank=True)
	color = models.ManyToManyField(Color, blank=True)
	tag = models.ManyToManyField(Tags)

	@property
	def real_price(self):
		return self.price - self.price * self.discount / 100

	@property
	def is_new(self):
		return (timezone.now() - self.created_at).days <= 3

	def __str__(self):
		return self.name


class ProductImages(BaseModel):
	photo = models.ImageField(upload_to="products/images/",
	                          validators=[FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'heic'])])
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")


class WishList(BaseModel):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

	class Meta:
		unique_together = ["product", "user"]
