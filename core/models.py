import json

from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

from image_tools.ocr import get_text
from itertools import takewhile, dropwhile, chain


def is_numeric_line(s):
    s = s.strip().replace(".", "").replace(",", "").replace(" ", "")
    return all(part.isdigit() for part in s)


def line_type(line):
    if is_numeric_line(line):
        if "." in line:
            pass


class ReceiptScan(TimeStampedModel):
    image = models.ImageField()
    raw = models.TextField(default="")
    full_text = models.TextField(default="")

    def scan_save_result(self):
        raw = get_text(self.image.read())
        if raw:
            self.raw = json.dumps(raw, indent=4)
            results = raw.get('textAnnotations', None)
            if results:
                self.full_text = results[0]['description']
        self.save()

    @property
    def parsed_result(self):
        if self.full_text:
            lines = self.full_text.splitlines()
            item_names = list(takewhile(lambda x: "CHF" not in x, lines))
            price_names = list(
                map(lambda x: x.strip().split(' '), list(dropwhile(lambda x: "CHF" not in x, lines))[1:]))

            flattened = list(chain(*price_names))
            #price_pairs = list(zip(flattened[::2], map(lambda x: x[0], flattened[1::2])))
            prices = list(filter(lambda x: "." in x, flattened))
            products = list(filter(lambda x: not is_numeric_line(x), item_names))

            if len(products) == len(prices):
                return list(zip(products, prices))
            return []
        else:
            return []
