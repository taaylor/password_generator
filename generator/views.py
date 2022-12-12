from django.shortcuts import render
from django.http import HttpResponse
import random
import string

# Create your views here.

def home(request):
    return render(request, 'generator/home.html')


def password(request):

    thepassword = ''

    
    s_alf_lower = [chr(i) for i in range(97, 123)]

    length = int(request.GET.get('length', 12))

    if request.GET.get('uppercase'):
        s_alf_lower.extend(string.ascii_uppercase) 
    
    if request.GET.get('special'): 
        s_alf_lower.extend(string.punctuation)

    if request.GET.get('numbers'):
        s_alf_lower.extend(string.digits)

    for _ in range(length):
        thepassword += random.choice(s_alf_lower)        
    

    return render(request, 'generator/password.html', {'password': thepassword})

def information(request):
    return render(request, 'generator/information.html')