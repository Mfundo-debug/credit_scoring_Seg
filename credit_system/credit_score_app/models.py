from django.db import models

# Create your models here.
class Customer(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    marital_status = models.CharField(max_length=10)
    education_level = models.CharField(max_length=10)
    employment_status = models.CharField(max_length=10)
    credit_utilization_ratio = models.FloatField()
    payment_history = models.CharField(max_length=10)
    number_of_credit_accounts = models.IntegerField()
    loan_amount = models.FloatField()
    interest_rate = models.FloatField()
    loan_term = models.IntegerField()
    type_of_loan = models.CharField(max_length=10)

    def __str__(self) -> str:
       # return all strings in the object
       return str(self.__dict__)

         
    