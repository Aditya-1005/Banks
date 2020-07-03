from django.contrib import admin
from .models import Banks,Branches


class BankDetails(admin.ModelAdmin):
    list_display = ['ID', 'Name']


admin.site.register(Banks,BankDetails)


class BrancDetails(admin.ModelAdmin):
    list_display = ['Bank_ID', 'IFSC', 'Branch', 'Address', 'City', 'District', 'State']


admin.site.register(Branches,BrancDetails)