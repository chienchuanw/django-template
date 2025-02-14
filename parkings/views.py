import csv, os
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.conf import settings
from typing import Any
from parkings.models import ParkingLot


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
            def __get_parking_name(id):
                parking_lot = ParkingLot.objects.filter(id=id).values("name").first()
                return parking_lot["name"] if parking_lot else "未知的停車場"

            parking_data = list(
                {
                    "id": int(row["ID"]),
                    "remain": (
                        0
                        if int(row["AVAILABLECAR"]) == -9
                        else int(row["AVAILABLECAR"])
                    ),
                    "name": __get_parking_name(int(row["ID"])),
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


class ParkingDetailView(DetailView):
    template_name = "parkings/detail.html"
    model = ParkingLot

    def __get_current_remain(self, id):
        CSV_FILE_PATH = os.path.join(
            settings.BASE_DIR, "data/input/新北市公有路外停車場即時賸餘車位數.csv"
        )
        try:
            with open(CSV_FILE_PATH, newline="", encoding="utf-8-sig") as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    if int(row["ID"]) == id:
                        return (
                            int(row["AVAILABLECAR"])
                            if int(row["AVAILABLECAR"]) > 0
                            else 0
                        )
                return 0
        except Exception as e:
            print(f"An error occurs during loading CSV: {e}")

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        # Get remain
        id = self.kwargs.get("pk")
        remain = self.__get_current_remain(id)

        # Get service_time and format text
        parking_lot = self.get_object()
        pay_ex = parking_lot.pay_ex.replace(";", "<br>") if parking_lot.pay_ex else ""

        context.update(
            {
                "remain": remain,
                "pay_ex": pay_ex,
            }
        )
        return context
