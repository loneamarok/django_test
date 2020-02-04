from django.shortcuts import render
from .models import App
# Create your views here.
def apps_webpage(request):
    apps = App.objects
    return render(request, 'apps/apps.html', {'apps': apps})
