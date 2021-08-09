from unittest import TestCase

from django.core.exceptions import ValidationError

from shop.products.validators import is_alpha_or_space_validator


class AlphaOrSpaceValidator(TestCase):
    def test_alphaorspaceValidator_shouldWork(self):
        is_alpha_or_space_validator('T t')
        self.assertTrue(True)

    def test_onlyAlpha_shouldWork(self):
        is_alpha_or_space_validator('Dddd')
        self.assertTrue(True)

    def test_AlphaOrSpace_shouldRaiseError(self):
        with self.assertRaises(ValidationError) as context:
            is_alpha_or_space_validator('D2 a@')
            self.assertEqual(str(context.exception), "Write a valid name.")
