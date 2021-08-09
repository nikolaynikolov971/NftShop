from django.core.exceptions import ValidationError


def only_letters_validator(value):
    result = all(c.isalpha() for c in value)
    if not result:
        raise ValidationError("City should contain only letters.")


def only_digits_validator(value):
    result = all(d.isdigit() for d in value)
    if not result:
        raise ValidationError("The phone number should contain only digits.")
