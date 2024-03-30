import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class userprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=50, default='',blank=True)
    address = models.CharField(max_length=50, default='',blank=True)
    phone = models.CharField(max_length=50, default='')
    country = models.CharField(max_length=50,default='0')
    avaliablebalance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    curentbalance = models.CharField(max_length=50,default='0')
    checkingbalance = models.CharField(max_length=50,default='10')
    accnumber = models.CharField(max_length=100,blank=True)
    acctype = models.CharField(max_length=10,blank=True)
    pair = models.CharField(max_length=10,blank=True,default='USD')
    image = models.FileField(default='pro_ny6h2o.png',blank=True)
    withdraw = models.BooleanField(default=False)
    
    def __str__(self):
        return self.fullname
        
class Deposit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deposit_slip = models.ImageField(upload_to='deposit')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Deposit - User: {self.user.username}, Amount: {self.amount}, Date: {self.timestamp}"

    
    
    

class TransactionHistory(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    TRANSACTION_TYPE_CHOICES = [
        ('deposit', 'Deposit'),
        ('withdrawal', 'Withdrawal'),
        ('transfer', 'Transfer'),
        # Add more transaction types as needed
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_type = models.CharField(max_length=100, choices=TRANSACTION_TYPE_CHOICES)
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    accountnumber = models.CharField(max_length=100)
    accountname = models.CharField(max_length=100)
    reference_number = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    

    def __str__(self):
        return f"Transaction for {self.user.username}"

    
class PIN(models.Model):
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    pin = models.CharField(max_length=6)

    def __str__(self):
        return f"PIN for {self.pin}"

class LocalWithdrawal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=100)
    iban = models.CharField(max_length=100)
    swiftcode = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Local Withdrawal - User: {self.user.username}, Amount: {self.amount}, Date: {self.date_created}"


class Withdraw(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    bank_address = models.CharField(max_length=100)
    narrate = models.CharField(max_length=100)
    bankname = models.CharField(max_length=100)
    accountname = models.CharField(max_length=100)
    accountnumber = models.CharField(max_length=100)
    iban = models.CharField(max_length=100)
    swift = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Withdrawal - User: {self.user.username}, Amount: {self.amount}, Date: {self.date_created}"

    
    
class Contact(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=100)
        
    def __str__(self):
        return self.name

class KYC(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    dob = models.DateField()
    ssn = models.CharField(max_length=20)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    id_type = models.CharField(max_length=50, choices=[
        ('passport', 'Passport'),
        ('national-id', 'National ID'),
        ('driver-licence', 'Driving License'),
    ])
    image1 = models.ImageField(upload_to='kyc/', blank=True)
    image2 = models.ImageField(upload_to='kyc/', blank=True)
    
    def __str__(self):
        return self.first_name


class LoanRequest(models.Model):
    amm = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.CharField(max_length=100)
    ten = models.IntegerField()
    pur = models.TextField()
    
    def __str__(self):
        return self.amm



#class TransactionHistory(models.Model):
#    user = models.ForeignKey(User, on_delete=models.CASCADE)
#    amount = models.DecimalField(max_digits=10, decimal_places=2)
#    status = models.CharField(max_length=20, default='Pending')
#    timestamp = models.DateTimeField(auto_now_add=True)#
#
#    def __str__(self):
#        return f"{self.user.username} - ${self.amount} - {self.status}"


