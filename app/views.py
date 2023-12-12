from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from .models import UserModel
from django.http import HttpResponse,JsonResponse


def home(request):
    return render(request, 'home.html')

# Create your views here.
def userRegistration(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        password = request.POST.get('password')
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('mailid')
        
        if len(phone) == 10:
            # obj = UserModel.objects.filter(email_id=email)
            # if obj:
            #     messages.warning(request, "You are already registered! Please, Use different Username and Email Address!")
            # else:
            register = UserModel(username=uname, password=password, first_name=fname, last_name=lname, address=address, phone_no=phone, email_id=email)
            try:
                register.save()
                messages.success(request, "Register Successfully! Now, You have to login...")
                # return redirect('home')
                return JsonResponse({'success': "Done!!!"}, status=200)
            except Exception as e:
                messages.warning(request, e)
        else:
            messages.warning(request, "Entered Mobile number not have 10 digits!")
                
        
    return render(request, 'UserRegister.html')
