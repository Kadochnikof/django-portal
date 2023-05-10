from django.urls import path
from . import views

app_name = 'instructions'
urlpatterns = [
    path('', views.instructions, name='instructions'),
    path('<int:instruction_id>', views.detail, name='detail')
]
