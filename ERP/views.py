from django.shortcuts import redirect, render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F                        #for OR operations
from django.http import HttpResponse
from StudentManagement.models import Student
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from StudentManagement.models import ToDoList, Task
from StudentManagement.forms import TaskForm

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
            messages.success(request, "You have been Logged In.")
            return redirect('home')
        else:
            messages.success(request, "There was an Error")
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


def todo_list(request):
    user = request.user  # Get the current logged-in user
    try:
        # Try to get the to-do list for the user
        todo_list = ToDoList.objects.get(user=user)
    except ToDoList.DoesNotExist:
        # If no to-do list exists, create one for the user
        todo_list = ToDoList.objects.create(user=user)

    tasks = todo_list.tasks.all()  # Retrieve all tasks in the user's to-do list

    # Debugging: print the tasks and their IDs to the console
    print("Tasks: ", [(task.taskID, task.taskName) for task in tasks])
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.todo_list = todo_list
            task.save()
            return redirect('todo_list')

    return render(request, 'todo_list.html', {'todo_list': todo_list, 'tasks': tasks, 'form': form})


# View to mark a task as complete/incomplete
def toggle_task_completion(request, task_id):
    task = get_object_or_404(Task,taskID=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('todo_list')


def delete_task(request, task_id):
    task = get_object_or_404(Task, taskID=task_id)
    task.delete()
    return redirect('todo_list')