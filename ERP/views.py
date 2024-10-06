from django.shortcuts import redirect, render
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F                        #for OR operations
from django.http import HttpResponse
from StudentManagement.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

@login_required
def say_truth(request):
    profile_set = Student.objects.all()
    return render(request, 'hello.html', {'students': profile_set})  # Pass the data as 'students'

def user_login(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            #messages.success(request, "You have been Logged In.")
            return redirect('home')
        else:
            #messages.success(request, "There was an Error")
            return redirect('login')
    else:
        return render(request, 'login.html')
 
def register_student(request):
    if request.method == 'POST':
        # Extract form data from the request
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        roll_no = request.POST.get('rollNo')
        phone_no = request.POST.get('phoneNo')
        address = request.POST.get('address')
        year = request.POST.get('year')
        division = request.POST.get('division')
        upi_id = request.POST.get('upiId')
        upi_handle = request.POST.get('upiHandle')

        # Create a new user in the default Django User model
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            first_name=first_name,
            last_name=last_name
        )
        
        # After user creation, create the Student object linked to this user
        student = Student.objects.create(
            user=user,
            name=f'{first_name} {last_name}',
            rollNo=roll_no,
            phoneNo=phone_no,
            address=address,
            year=year,
            division=division,
            upiId=upi_id,
            upiHandle=upi_handle
        )
        
        # Redirect or render success page
        return redirect('home')  # Update with your desired redirect page

    # If the request method is GET, display the form page
    return render(request, 'register.html')