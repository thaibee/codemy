from django.db import models


class ClubUsers(models.Model):
    f_name = models.CharField('First Name', max_length=30)
    l_name = models.CharField('Last name', max_length=30)
    email_address = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return self.f_name + ' ' + self.l_name


class Venue(models.Model):
    name = models.CharField('Name of Venue', max_length=30)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=25)
    web_address = models.URLField(max_length=50)
    email_address = models.EmailField(max_length=50)

    def __str__(self):
        return self.name


class Events(models.Model):
    name = models.CharField(max_length=30)
    event_date = models.DateField
    event_time = models.TimeField
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    manager = models.CharField(max_length=30)
    attendees = models.ManyToManyField(ClubUsers)

    def __str__(self):
        return self.name
