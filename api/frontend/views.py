from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def list(request):
    return render(request,'index.html')




def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('list')  
        else:
            # Handle invalid login credentials
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    return render(request, 'login.html')


