from django.db import models

from django.db import models

from general.models import BaseModel


class Banner(BaseModel):
	collection = models.CharField(max_length=33)
	title = models.CharField(max_length=51)
	description = models.TextField()
	photo = models.ImageField(upload_to="pages/banners/")
	status = models.BooleanField(default=False)

	def __str__(self):
		return f"{self.collection}"

	class Meta:
		verbose_name = "Banner"
		verbose_name_plural = "Banners"
