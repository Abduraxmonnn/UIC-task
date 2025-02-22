from main.models import Product
from django.db.models.functions import Upper
from django.db import connection
from django.db.models import Count
from pprint import pprint
import random


def run():
    qs = Product.objects.all().aggregate(Count("pk"))
    pprint(qs)
    pprint(connection.queries)

    if not isinstance(qs, dict):
        for i, x in enumerate(qs):
            if i == 0:
                pprint(list(x.__dict__)[1:])
            pprint(list(x.__dict__.values())[1:])
