from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from academics.models import *
from .models import *

def create_applicant(request):
    if request.method == 'POST':
        form = PreApplicationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Create User instance but don't save it to the database yet
            user.is_applicant = True
            user.save()
            course_of_study = form.cleaned_data.get('course_name')
            pre_application_form_data = form.cleaned_data  # Get the form data as a dictionary
            pre_application_form_data.pop('course_name')  # Remove 'course_name' from the data since it's not part of User model
            Applicant.objects.create(applicant=user, course_name=course_of_study)
            messages.success(request, 'Account created Successfully.')
            return redirect('user_login')
    else:
        form = PreApplicationForm()

    context = {
        'form': form,
        'page_title': 'Pre-Application',
    }

    return render(request, 'admission/pre_application.html', context)

