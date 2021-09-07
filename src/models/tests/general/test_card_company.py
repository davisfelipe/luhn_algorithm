from unittest import TestCase

from src.models.general import Company


class CardCompanyModels(TestCase):

    def test_company_model_values(self):
        self.assertEqual(Company.AMEX.value, "american express")
        self.assertEqual(Company.MASTER.value, "mastercard")
        self.assertEqual(Company.VISA.value, "visa")
        self.assertEqual(Company.UNKNOWN.value, "unknown")
