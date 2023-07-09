import requests
from django.conf import settings


def calculate(income):
    base_url = settings.ENGINE_BASE_URL
    response = requests.get(
        f"{base_url}/calculate",
        params={
            "income": income,
        },
    )
    return response.json()
