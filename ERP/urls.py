#Map Our Urls to view Function
#It is a URL Configuration Module
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.say_truth, name="home"),
    path('', views.user_login, name="login"),
    path('register/', views.register_student, name="sregister"),
    # Dont Need 'playground/hello' as already defined in storefronts "urls.py"
    path('todo/', views.todo_list, name='todo_list'),
    path('todo/toggle/<int:task_id>/', views.toggle_task_completion, name='toggle_task_completion'),
    path('todo/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('announcement/', views.user_groups_announcements),
    path('Stationary/', views.seller_items),
    path('store/', views.store_view, name='store_view'),
    path('create-group/', views.create_group, name='create_group'),
    path('group-list/', views.group_list, name='group_list'),  # Add this URL pattern
    path('create-announcement/', views.create_announcement, name='create_announcement'),
]