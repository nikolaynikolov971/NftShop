from unittest import TestCase

from django.core.exceptions import ValidationError

from shop.profiles.validators import only_digits_validator


class OnlyDigitsValidator(TestCase):
    def test_whenItsOnlyDigits_andItWorks(self):
        only_digits_validator('323')
        self.assertTrue(True)

    def test_whenItShouldThrowValidationError(self):
        with self.assertRaises(ValidationError) as context:
            only_digits_validator('1@a1')
            self.assertEqual(str(context.exception), "The phone number should contain only digits.")