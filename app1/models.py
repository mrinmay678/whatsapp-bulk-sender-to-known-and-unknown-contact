from django.db import models

# Create your models here.


class PhoneNumberCSV(models.Model):
    file_name = models.FileField(upload_to='phonecsv')
    used = models.BooleanField(default=False)

    def __str__(self):
        return "file"+str(self.id)


class PhoneNumber(models.Model):
    phonenumber = models.IntegerField()
    message = models.CharField(max_length=256)
