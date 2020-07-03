from django.db import models


class Banks(models.Model):
    ID = models.CharField(primary_key=True,max_length=10)
    Name = models.CharField(max_length=50)
    def __str__(self):
        return self.ID


class Branches(models.Model):
    Bank_ID = models.ForeignKey(Banks,related_name='branches',on_delete=models.CASCADE)
    IFSC = models.CharField(max_length=11)
    Branch = models.CharField(max_length=75)
    Address = models.CharField(max_length=200)
    City = models.CharField(max_length=100)
    District = models.CharField(max_length=100)
    State = models.CharField(max_length=100)



