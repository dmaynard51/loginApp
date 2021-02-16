from django.http.response import HttpResponse, HttpResponseRedirect
from basic_app.forms import UserProfileInfoForm
from django.shortcuts import render
from basic_app.forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
import openpyxl

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

#second commit