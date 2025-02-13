import csv, os
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.conf import settings


class ParkingIndexView(TemplateView):
    template_name = "parkings/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # specify CSV path
        csv_file_path = os.path.join(
            settings.BASE_DIR, "data/input/新北市公有路外停車場即時賸餘車位數.csv"
        )

        # read and load CSV
        with open(csv_file_path, newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.reader(csvfile)
            headers = next(reader)
            data_list = list(row for row in reader)

        # re-assemble data from CSV
        parking_data = [
            {
                "name": "test",
                "id": int(parking_id),
                "status": (
                    "Error"
                    if int(remain) == -9
                    else "None" if int(remain) == 0 else "Available"
                ),
                "remain": int(remain) if int(remain) > 9 else 0,
            }
            for parking_id, remain in data_list
        ]

        # send to html as context
        context["headers"] = headers
        context["parking_data"] = parking_data

        return context
