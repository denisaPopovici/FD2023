from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_all_students),
    path('new-student/', views.add_student),
    path('remove-student/<str:code>/', views.delete_student),
    path('update-student/<str:code>/', views.update_student)
]