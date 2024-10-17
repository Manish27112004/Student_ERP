from django.shortcuts import redirect, render, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q,F                        #for OR operations
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from StudentManagement.models import ToDoList, Task, Group, Announcement, Stationary, Student, SharingIsCaringStore, Teacher
from StudentManagement.forms import TaskForm, GroupForm, AnnouncementForm
from django.core.exceptions import PermissionDenied


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


def user_groups_announcements(request):
    # Get the logged-in user
    user = request.user

    # Get the groups the user belongs to (assuming the user is a student)
    groups = Group.objects.filter(students=user.student)

    # Get announcements for these groups
    announcements = Announcement.objects.filter(group__in=groups).order_by('-timestamp')

    # Pass the groups and announcements to the template
    context = {
        'groups': groups,
        'announcements': announcements,
    }

    return render(request, 'announcement.html', context)


def seller_items_view(request):
    # Fetch all stationary items along with their sellers
    items = Stationary.objects.select_related('seller').all()
    
    context = {
        'items': items,
    }
    return render(request, 'seller_items.html', context)


def store_view(request):
    items = SharingIsCaringStore.objects.all()  # Get all items in the store
    return render(request, 'store_items.html', {'items': items})


@login_required
def create_group(request):
    try:
        # Check if the user has a related teacher object
        teacher = request.user.teacher
    except Teacher.DoesNotExist:
        # If the user is not a teacher, raise a permission error or handle accordingly
        raise PermissionDenied("You are not authorized to create a group because you are not a teacher.")
    
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.teacher = teacher  # Assign the logged-in teacher to the group
            group.save()
            form.save_m2m()  # Save the many-to-many field (students)
            return redirect('group_list')
    else:
        form = GroupForm()
    
    return render(request, 'create_group.html', {'form': form})


@login_required
def group_list(request):
    try:
        teacher = request.user.teacher  # Get the teacher associated with the current user
        groups = Group.objects.filter(teacher=teacher)  # Filter groups created by this teacher
    except Teacher.DoesNotExist:
        groups = []  # If the user is not a teacher, return an empty list or handle as needed
    
    return render(request, 'group_list.html', {'groups': groups})


@login_required
def create_announcement(request):
    teacher = request.user.teacher  # Get the teacher associated with the logged-in user
    
    if request.method == 'POST':
        form = AnnouncementForm(request.POST, teacher=teacher)  # Pass teacher to the form
        if form.is_valid():
            announcement = form.save(commit=False)
            announcement.teacher = teacher  # Link the announcement to the logged-in teacher
            announcement.save()
            return redirect('group_list')  # Redirect after successful creation
    else:
        form = AnnouncementForm(teacher=teacher)  # Pass teacher to the form
    
    return render(request, 'create_announcement.html', {'form': form})