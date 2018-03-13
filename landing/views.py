from django.contrib import auth
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, BadHeaderError, HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'landing/index.html', locals())




