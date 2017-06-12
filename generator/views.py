from random import choices

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def test(request):
    return HttpResponse('Hello, I am a generator! yeah.')
