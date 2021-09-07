from unittest import TestCase

from fastapi.responses import UJSONResponse as FastAPIResponse

from src.utils.response import UJSONResponse


class ResponseTest(TestCase):

    def test_response(self):
        response = UJSONResponse("message", 5)
        self.assertIsInstance(response, FastAPIResponse)
        self.assertIsInstance(response.status_code, int)
