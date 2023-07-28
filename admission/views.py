from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth.decorators import login_required

def create_applicant(request):
    form = PreApplicationForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.is_applicant = True
            user.save()
            return redirect('home')
    else:
        form = PreApplicationForm()

    return render(request, 'pre_application.html', {'form': form})
