from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'index.html',context={})

def studymaterial(request):
    return render(request,'studymaterial.html',context={})

def ourinterns(request):
    return render(request, 'ourinterns.html',context={})

def aboutus(request):
    return render(request, 'aboutus.html', context={})

