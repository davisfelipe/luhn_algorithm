from dataclasses import dataclass


@dataclass
class CreditCardMessage:
    valid: str = "Valid credit card number"
    invalid: str = "Invalid credit card number"
