from django.urls import path
from . import views


 
urlpatterns = [
     path('admission/pre-application/', views.create_applicant, name='create_applicant'),

]