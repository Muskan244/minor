from django.db import models

# Create your models here.
class PNR(models.Model):
    pnr_number = models.CharField(max_length=10, unique=True)
    is_valid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.pnr_number} - Valid: {self.is_valid}"