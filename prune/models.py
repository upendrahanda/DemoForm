from django.db import models

currency_choices = (('1', 'INR'), ('2', 'USD'))
country_choices = (('1', "India"), ('2', 'USA'))


class Transactions(models.Model):
    name = models.CharField(max_length=45)
    ph_no = models.PositiveIntegerField()
    country = models.CharField(choices=country_choices, max_length=1, default='1')
    currency_rx = models.CharField(choices=currency_choices, max_length=1, default='1')
    currency_tx = models.CharField(choices=currency_choices, max_length=1, default='1')
