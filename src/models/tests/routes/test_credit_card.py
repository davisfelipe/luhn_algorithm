from unittest import TestCase

from pydantic import BaseModel

from src.models.routes import InputCreditCard


class InputCreditCardTest(TestCase):

    def test_input_credit_card(self):
        result = InputCreditCard(number="4281138482933123")
        self.assertIsNotNone(result)
        self.assertIsInstance(result, BaseModel)

    def test_input_credit_card_exception(self):
        with self.assertRaises(ValueError):
            InputCreditCard(number="138482933123")

        with self.assertRaises(ValueError):
            InputCreditCard(number="1384a2933123")
