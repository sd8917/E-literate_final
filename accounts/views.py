from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'accounts/signup.html',context={})

def login(request):
    return render(request, 'accounts/login.html',context={})


