from django.db import models


class EmailFind(models.Model):
    open_email = models.BooleanField(default=False)
