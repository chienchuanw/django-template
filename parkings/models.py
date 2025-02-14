from django.db import models


class ParkingLot(models.Model):
    PARKING_TYPE_CHOICES = [
        (1, "剩餘車位數"),
        (2, "靜態停車場資料"),
    ]

    id = models.SmallIntegerField(primary_key=True, unique=True)
    area = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    type = models.SmallIntegerField(choices=PARKING_TYPE_CHOICES)
    summary = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=255)
    tel = models.CharField(max_length=20, blank=True, null=True)
    pay_ex = models.TextField(blank=True, null=True, verbose_name="pay info")
    service_time = models.CharField(max_length=255, blank=True, null=True)
    tw97x = models.FloatField(blank=True, null=True, verbose_name="x-coordinate")
    tw97y = models.FloatField(blank=True, null=True, verbose_name="y-coordinate")
    total_car = models.SmallIntegerField(blank=True, null=True)
    total_motor = models.SmallIntegerField(blank=True, null=True)
    total_bike = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.id}"
