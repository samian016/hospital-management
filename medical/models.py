from django.db import models

# Create your models here.


class Patient(models.Model):
    date = models.DateField()
    release_date = models.DateField(null=True)
    status = models.TextField()
    first_name = models.TextField()
    second_name = models.TextField()
    date_of_birth = models.DateField()
    sex = models.TextField()
    maritalS = models.TextField()
    childrenN = models.IntegerField()
    residence = models.TextField()
    nationality = models.TextField()
    occupation = models.TextField()
    religion = models.TextField()
    guardian_first_name = models.TextField()
    guardian_second_name = models.TextField()
    telephone = models.TextField()
    disease = models.TextField()
    ward = models.TextField()
    bed = models.IntegerField()
    care_note = models.TextField()
    transfer_from = models.TextField()
    pulse = models.IntegerField()
    bloodP = models.IntegerField()
    respiration = models.IntegerField()
    tempe = models.IntegerField()
    physical_con = models.TextField()
    death_date = models.DateField(null=True)
    case_summary = models.TextField(null= True)
