# this filecreated by me - Akash patel

# importing https for https response
from django.http import HttpResponse

# import rander from django.shortcuts to render templates files
from django.shortcuts import render 


# here we only giving response by string
# def home(response):
#     return HttpResponse("Hello")

# here we only giving response by html
def home(request):
    return render(request,'index.html')

# for result where all info displyed
def result(request):

    # catching form info on variable
    firstname = request.GET.get('firstname', 'default')
    lastname = request.GET.get('lastname', 'default')
    email = request.GET.get('email', 'default')
    password = request.GET.get('password', 'default')
    address = request.GET.get('address', 'default')

    # created a dictonary to gve info in result
    container = {'firstname': firstname, 'lastname': lastname, 'email':email,'password':password,'address':address}
    return render(request, 'result.html', container)