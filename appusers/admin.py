from django.contrib import admin
from .models import  *
# Register your models here.





admin.site.register(userprofile)
admin.site.register(Deposit)
admin.site.register(PIN)
admin.site.register(LocalWithdrawal)
admin.site.register(KYC)
admin.site.register(Withdraw)
admin.site.register(LoanRequest)
admin.site.register(TransactionHistory)
admin.site.register(Contact)




