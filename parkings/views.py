import csv, os
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.conf import settings
from typing import Any


class ParkingIndexView(TemplateView):
    template_name = "parkings/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # specify CSV path
        CSV_FILE_PATH = os.path.join(
            settings.BASE_DIR, "data/input/新北市公有路外停車場即時賸餘車位數.csv"
        )

        # read and load CSV
        with open(CSV_FILE_PATH, newline="", encoding="utf-8-sig") as csvfile:
            # reader = csv.reader(csvfile)
            reader = csv.DictReader(csvfile)

            # re-assemble data from CSV
            parking_data = list(
                {
                    "id": int(row["ID"]),
                    "remain": (
                        0
                        if int(row["AVAILABLECAR"]) == -9
                        else int(row["AVAILABLECAR"])
                    ),
                    "name": "test",
                    "status": (
                        "Error"
                        if int(row["AVAILABLECAR"]) == -9
                        else "None" if int(row["AVAILABLECAR"]) == 0 else "Available"
                    ),
                }
                for row in reader
            )

        # send to html as context
        context.update(
            {
                "parking_data": parking_data,
            }
        )

        return context


class ParkingDetailView(TemplateView):
    template_name = "parkings/detail.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        CSV_FILE_PATH = os.path.join(
            settings.BASE_DIR, "data/input/新北市路外公共停車場資訊.csv"
        )

        with open(CSV_FILE_PATH, newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile)
            header = next(reader)
            content = list(row for row in reader)

        context.update(
            {
                "header": header,
                "content": content,
            }
        )
        return context
