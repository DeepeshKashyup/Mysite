from django.shortcuts import render

def index(request):
    return render(request, 'Portfolio/home.html')

def contact(request):
    return render(request, 'Portfolio/basic.html',{'content':['You can contact me on my email address','deepesh@mail.usf.edu']})

