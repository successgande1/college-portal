from django.shortcuts import render, redirect,  get_object_or_404
from . models import *
from . forms import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import get_user, get_user_model
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
def custom_page_not_found(request, exception=None):
    return render(request, 'accounts/404.html', status=404)