from django.shortcuts import render
from .models import Banks,Branches
from mybank import forms
from .serializers import BankSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
from django.http import HttpResponse

# Functionality if in case anyone other than admin wants to add a Bank
'''def add_bank(request):
    if request.method == 'POST':
        form = forms.BankForm(request.POST or None)
        if form.is_valid():
            bank_id = form.cleaned_data['ID']
            name = form.cleaned_data['Name']

            bank = Banks(ID=bank_id,Name=name)
            bank.save()
    else:
        form = forms.BankForm()
    return render(request,'mytemplates/bank.html',{'form':form})
'''
# Functionality if in case anyone other than admin wants to add a Branch
'''def add_branch(request):
    if request.method == 'POST':
        form = forms.BranchForm(request.POST or None)
        if form.is_valid():
            bank_id = form.cleaned_data['Bank_ID']
            ifsc = form.cleaned_data['IFSC']
            branch = form.cleaned_data['Branch']
            address = form.cleaned_data['Address']
            city = form.cleaned_data['City']
            district = form.cleaned_data['District']
            state = form.cleaned_data['State']

            branch = Branches(Bank_ID=bank_id,IFSC=ifsc,Branch=branch,Address=address,City=city,District=district,State=state)
            branch.save()
    else:
        form = forms.BranchForm()
    return render(request,'mytemplates/branch.html',{'form':form})
'''

# API
class BankList(APIView):

    def get(self,request):
        banks = Banks.objects.all()
        serializer = BankSerializer(banks,many=True)
        return Response(serializer.data)


# If user enters the IFSC code, all the details related to the branch are displayed.
def ifsc(request):
    url = 'http://127.0.0.1:8000/apiview'
    json_object = requests.get(url).json()
    ifsc_code = request.POST.get('ifsc')
    print(ifsc_code)
    bank_list = []
    if ifsc_code != 'None':
        if request.method == 'POST':
            for item in json_object:
                for branch in item['branches']:
                    if branch['IFSC'] == ifsc_code:

                        bank = {
                                'Bank': item['Name'],
                                'ID': item['ID'],
                                'IFSC': branch['IFSC'],
                                'Branch': branch['Branch'],
                                'Address': branch['Address'],
                                'City': branch['City'],
                                'District': branch['District'],
                                'State': branch['State']
                            }
                        bank_list.append(bank)
                    else:

                        bank={
                            'Bank': 'No Record',
                            'ID': 'No Record',
                            'IFSC': 'No Record',
                            'Branch': 'No Record',
                            'Address': 'No Record',
                            'City': 'No Record',
                            'District': 'No Record',
                            'State': 'No Record'
                        }

        print(bank_list)
        msg = 'No Branch found!!Enter valid IFSC code!!'
        return render(request,'mytemplates/ifsc.html',{'banks':bank_list,'msg':msg})
    return render(request, 'mytemplates/ifsc.html')


# If user enters Bank and City, all the details related to the all the branches in that City are displayed.
def bank_city(request):
    url = 'http://127.0.0.1:8000/apiview'

    json_object = requests.get(url).json()
    bank = request.POST.get('bank', False)
    city = request.POST.get('city', False)
    if bank != False and city != False:
        if request.method == 'POST':

            branch_list = []
            for item in json_object:
                if item['Name'] == bank:
                    for branch in item['branches']:
                        if branch['City'] == city:
                            branch_dict = {
                                'Name': item['Name'],
                                'ID': item['ID'],
                                'IFSC': branch['IFSC'],
                                'Branch': branch['Branch'],
                                'Address': branch['Address'],
                                'City': branch['City'],
                                'District': branch['District'],
                                'State': branch['State'],

                            }
                            branch_list.append(branch_dict)
        msg = 'The Bank does not have any branches in your city!!'
        return render(request,'mytemplates/bank_city.html',{'branches':branch_list,'msg':msg})
    return render(request,'mytemplates/bank_city.html')

def ifsc_view(request):
    return render(request,'mytemplates/ifsc.html')