from django.http.response import HttpResponse, HttpResponseRedirect
from basic_app.forms import UserProfileInfoForm
from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import openpyxl
from basic_app.models import invoices
from django.db.models import Sum
from django.db import connection

# Create your views here.

def index(request):

    excel_data = list()
    if request.method == "POST":
        excel_file = request.FILES["excel_file"]

        wb = openpyxl.load_workbook(excel_file)

        worksheet= wb['Sheet1']
        print(worksheet)


        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            

            invoice = invoices.objects.get_or_create(customer_number=row_data[0], customer_name=row_data[1], invoice_number=row_data[2], 
            invoice_date = row_data[3], due_date = row_data[4], salesOrder_number= row_data[5], 
            amount_due = row_data[6], current_balance= row_data[7], past_due_1_30= row_data[8],
            past_due_31_60=row_data[9], over_90=row_data[10], jde_customer_number=row_data[11],
            business_unit=row_data[12], rep=row_data[13], netdays=row_data[14], custType=row_data[15], 
            custCode=row_data[16],custGroup3=row_data[17], custPO=row_data[18])[0]
            
            invoice.save()
            excel_data.append(row_data)


    return render(request, 'basic_app/index.html', {'excel_data' : excel_data})

def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)


        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                print('Found it')

                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
        
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'basic_app/registration.html', {'registered' : registered, 'profile_form': profile_form, 'user_form': user_form})




@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


    

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)

                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponseRedirect("your Account is not active")
        else:
            return HttpResponseRedirect("Invalid login details")

    else:
        #nothing entered
        return render(request, 'basic_app/user_login.html', {})    


def account_page(request):
    all_invoices = invoices.objects.values('customer_number', 'customer_name') \
        .annotate(total_amount_due=Sum('amount_due'))
    print (all_invoices)
    return render(request, 'basic_app/account_page.html', {"all_invoices": all_invoices})