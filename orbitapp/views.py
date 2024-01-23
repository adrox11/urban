from urllib import request

from django.http import HttpResponse
from django.shortcuts import render
from .models import apple


# Create your views here.
def demo(request):
    obj = apple.objects.all()

    return render(request, "index.html", {'result': obj})

# def home(request):
#  return render(request, "home.html")


# def addition(request):
#  x = int(request.GET['num1'])
#  y = int(request.GET['num2'])
#  res = x + y

#  sub = x - y
#  mul = x * y

#  div = x / y if y != 0 else 'not possible to divide by zero'

# return render(request, "results.html", {
# 'result': res,
# 'subtraction': sub,
# 'multiplication': mul,
# 'division': div
# })
