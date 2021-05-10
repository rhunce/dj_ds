from django.shortcuts import render

# Create your views here.


def home_view(request):
    hello = 'hello world from the view'
    return render(request, 'sales/main.html', {'hello': hello})
