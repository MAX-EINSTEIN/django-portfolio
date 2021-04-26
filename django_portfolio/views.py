from django.shortcuts import redirect

# Create your views here.
def redirect_root(request):
    return redirect('index')