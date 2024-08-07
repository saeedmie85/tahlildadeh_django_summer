from . import jalali
from django.utils import timezone


def jalali_converter(time):
    time = timezone.localtime(time)

    time_to_str = f"{time.year},{time.month},{time.day}"
    time_to_list = list(jalali.Gregorian(time_to_str).persian_tuple())
    months = [
        "فروردین",
        "اردیبهشت",
        "خرداد",
        "تیر",
        "مرداد",
        "شهریور",
        "مهر",
        "آبان",
        "آذر",
        "دی",
        "بهمن",
        "اسفند",
    ]
    time_to_list[1] = months[time_to_list[1] - 1]
    output = f"{time_to_list[2]} {time_to_list[1]} {time_to_list[0]} ساعت {time.hour}:{time.minute}"
    return output
