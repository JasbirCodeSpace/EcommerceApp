from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=13)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    def __str__(self):
        return self.email
    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.filter(email=email).first()
        except:
            return False
    @staticmethod
    def get_customer_by_id(id):
        try:
            return Customer.objects.filter(id=id).first()
        except:
            return False
    @staticmethod
    def is_exist(email):
        if Customer.objects.filter(email = email):
            return True
        return False