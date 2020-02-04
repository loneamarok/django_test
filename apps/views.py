from django.shortcuts import render

# Create your views here.
def apps_webpage(request):
     return render(request, 'apps/app_webpage.html')
