from unittest import TestCase

from src.use_case import ValidateCreditCard
from src.use_case.credit_card_use_case import CardResponse


class ValidateCreditCardTest(TestCase):

    def test_valid_credit_card(self):
        response = ValidateCreditCard.handle("4916652732894780")

        self.assertIsNotNone(response)
        self.assertIsInstance(response, CardResponse)
        self.assertEqual(response.code, 200)

        data_expected = dict(company="visa")
        self.assertDictEqual(response.data, data_expected)

    def test_invalid_credit_card(self):
        response = ValidateCreditCard.handle("123456780987")

        self.assertIsNotNone(response)
        self.assertIsInstance(response, CardResponse)
        self.assertEqual(response.code, 400)
