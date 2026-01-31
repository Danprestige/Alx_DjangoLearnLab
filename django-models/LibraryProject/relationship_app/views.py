from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView

# Login view
class LoginView(DjangoLoginView):
    template_name = 'relationship_app/login.html'

# Logout view
class LogoutView(DjangoLogoutView):
    template_name = 'relationship_app/logout.html'

# Registration view
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # after registration, go to login
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


