from unittest import TestCase

from django.core.exceptions import ValidationError

from shop.profiles.validators import only_letters_validator


class test_OnlyLetterValidator_henItSholdWork(TestCase):
    def test_whenItWorks(self):
        only_letters_validator('dsad')
        self.assertTrue(True)

    def test_whenItShouldNotWork(self):
        with self.assertRaises(ValidationError) as context:
            only_letters_validator('d2d')

            self.assertEqual(str(context.exception), "City should contain only letters.")
