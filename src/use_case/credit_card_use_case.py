from dataclasses import dataclass
from typing import Optional

from starlette.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from src.models.general import Company
from src.utils.messages import CreditCardMessage


@dataclass
class CardResponse:
    message: str
    code: int
    data: Optional[dict] = None


class ValidateCreditCard:

    @classmethod
    def handle(cls, number: str) -> CardResponse:
        if not cls._verify_luhn_algorithm(number):
            return CardResponse(CreditCardMessage.invalid, HTTP_400_BAD_REQUEST)

        data = cls._find_credit_card_information(number)

        return CardResponse(CreditCardMessage.valid, HTTP_200_OK, data)

    @classmethod
    def _verify_luhn_algorithm(cls, number: str) -> bool:
        """
        Verify if input is a valid number according to Luhn algorithm.

        :param number: input number to validate.
        :return: if is a valid number or not.
        """
        num_list = [int(integer) for integer in number]

        # Invert number and duplicate all odd numbers according to the
        # algorithm.
        odd_digits = [sum(divmod(d * 2, 10)) for d in num_list[-2::-2]]
        return sum(num_list[::-2] + odd_digits) % 10 == 0

    @classmethod
    def _find_credit_card_information(cls, number: str) -> dict:
        """
        Get credit card information as company name:

        :param number: credit card number.
        :return: credit card information.
        """
        credit_card_business = {
            5: Company.MASTER,
            4: Company.VISA,
            3: Company.AMEX,
        }
        data = dict(
            company=credit_card_business.get(
                int(number[0]),
                Company.UNKNOWN
            ).value
        )
        return data
