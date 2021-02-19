from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
def register(request):
    if request.method == 'POST':
        # name = request.form['name']
        # email = request.form['email']
        # print(name,email)
        print('hitting post route')
    return HttpResponse('hello')