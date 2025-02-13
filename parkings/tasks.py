import os, requests
from celery import shared_task
from django.conf import settings

CSV_URL = "https://data.ntpc.gov.tw/api/datasets/e09b35a5-a738-48cc-b0f5-570b67ad9c78/csv/file"
CSV_FILE_PATH = os.path.join(
    settings.BASE_DIR, "data/input/新北市公有路外停車場即時賸餘車位數.csv"
)


@shared_task
def update_csv():
    """
    Download the latest parking space data from government's API
    Load the data and overwrite the existing CSV file
    """

    response = requests.get(CSV_URL)
    if response.status_code == 200:
        with open(CSV_FILE_PATH, "wb") as f:
            f.write(response.content)

        # This return message will be documented in Celery Worker terminal log
        return "Successfully update the CSV"

    return "Fail to update the CSV"
