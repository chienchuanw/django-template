from django.core.management.base import BaseCommand
import os, csv
from django.conf import settings
from parkings.models import ParkingLot
from django.db import transaction


class Command(BaseCommand):
    help = "Import data of parking lots CSV to database"

    def handle(self, *args, **options):
        CSV_FILE_PATH = os.path.join(
            settings.BASE_DIR, "data/input/新北市路外公共停車場資訊.csv"
        )

        if not os.path.exists(CSV_FILE_PATH):
            self.stdout.write(
                self.style.ERROR(f"Cannot find CSV file: {CSV_FILE_PATH}")
            )
            return

        with open(CSV_FILE_PATH, newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)

            parking_lots = list()

            for row in reader:
                try:
                    parking_lot = ParkingLot(
                        id=int(row["ID"]),
                        area=row["AREA"].strip(),
                        name=row["NAME"].strip(),
                        type=int(row["TYPE"]),
                        summary=row["SUMMARY"].strip() or None,
                        address=row["ADDRESS"].strip() or None,
                        tel=row["TEL"].strip() or None,
                        pay_ex=row["PAYEX"].strip() or None,
                        service_time=row["SERVICETIME"].strip() or None,
                        tw97x=float(row["TW97X"]) if row["TW97X"] else None,
                        tw97y=float(row["TW97Y"]) if row["TW97Y"] else None,
                        total_car=int(row["TOTALCAR"]),
                        total_motor=int(row["TOTALMOTOR"]),
                        total_bike=int(row["TOTALBIKE"]) if row["TOTALBIKE"] else None,
                    )

                    parking_lots.append(parking_lot)
                except ValueError as err:
                    self.stderr.write(
                        self.style.WARNING(f"Skip invalid data: {row} - {err}")
                    )

        if parking_lots:
            with transaction.atomic():
                ParkingLot.objects.bulk_create(parking_lots, ignore_conflicts=True)

            self.stdout.write(
                self.style.SUCCESS(f"Successfully import {len(parking_lots)} data")
            )

        else:
            self.stderr.write(self.style.ERROR(f"No valid data can be imported"))
