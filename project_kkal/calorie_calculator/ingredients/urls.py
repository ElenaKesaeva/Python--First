
from django.urls import path
from . import views
from .views import index, details, LogoutView, LoginView, register

app_name = "ingredients"

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('<int:pk>/', details, name='details'),
    path('outcome/', views.ingredient_outcome_view, name='outcome'),
    path('outcome/delete/<int:ingredient_id>', views.ingredient_delete, name='ingredient_delete'),
    ]
