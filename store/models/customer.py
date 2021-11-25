from django.db import models

# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=500)

    # this function featch email from database and store in email varible
    # in email varible we get email if it in datatbase then true other wise it false
    def User_Exists(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False

    @staticmethod
    # this function is use to find that user email is there in database or not
    # write this code in try & except 
    # because in this case we will get true or you can say result(email) 
    # or other wise it will be false. false mean no email that way we get error
    def User_Email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False


    def __str__(self):
        return self.firstname
