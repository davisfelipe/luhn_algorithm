from fastapi import FastAPI
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR

from src.models import InputCreditCard
from src.use_case import ValidateCreditCard
from src.utils.response import UJSONResponse

app = FastAPI()


@app.post('/credit_card/validate')
def validate_credit_card(credit_card: InputCreditCard):
    try:
        response = ValidateCreditCard.handle(credit_card.number)
        return UJSONResponse(response.message, response.code, response.data)
    except Exception as error:
        return UJSONResponse(str(error), HTTP_500_INTERNAL_SERVER_ERROR)
