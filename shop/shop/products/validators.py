from django.core.exceptions import ValidationError


def is_alpha_or_space_validator(value):
    result = all(c.isalpha() or c.isspace() for c in value)
    if not result:
        raise ValidationError("Write a valid name.")
