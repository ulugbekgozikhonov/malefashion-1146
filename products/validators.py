from django.core.exceptions import ValidationError


def validator_rating(rating):
	if not (1 <= rating <= 5):
		raise ValidationError("Rating must be 1 and 5")
