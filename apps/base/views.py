from django.shortcuts import render
from apps.base import models as bases
from apps.secondary import models as secondarys
# Create your views here.
def index(request):
    user_info = bases.User.objects.latest("id")
    settings = secondarys.Settings.objects.latest("id")
    header = bases.Header.objects.latest("id")
    return render(request, 'index-4.html', locals())