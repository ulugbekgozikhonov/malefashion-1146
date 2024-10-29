from django.core.exceptions import ValidationError


def validator_rating(value):
	if not (1 <= value <= 5):
		raise ValidationError("Rating must be between 1 and 5")
