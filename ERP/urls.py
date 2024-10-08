#Map Our Urls to view Function
#It is a URL Configuration Module
from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.say_truth, name="home"),
    path('login/', views.user_login, name="login"),
    path('register/', views.register_student, name="sregister"),
    # Dont Need 'playground/hello' as already defined in storefronts "urls.py"
    path('todo/', views.todo_list, name='todo_list'),
    path('todo/toggle/<int:task_id>/', views.toggle_task_completion, name='toggle_task_completion'),
    path('todo/delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('announcement/', views.user_groups_announcements),
    path('Stationary/', views.seller_items_view),
    path('store/', views.store_view, name='store_view'),
]