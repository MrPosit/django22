from django.shortcuts import render
from .models import Account
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.http import HttpResponse
import random

def home(request):
    all_users = User.objects.all()
    return render(request, 'home.html', {'users': all_users})

def random_numbers():
    result = ''
    for i in range(1,20):
        if i % 5 == 0 and i != 0:
            result += ' '
            continue
        result += str(random.choice(range(10)))
    return result

class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    
    def form_valid(self, form):
        with transaction.atomic():
            response = super().form_valid(form)
            try:
                if random.choice([True, False]):
                    raise Exception("An error occurred, rolling back transaction")
                Account.objects.create(number=random_numbers(), owner=self.object)
            except Exception as e:
                transaction.set_rollback(True)
                return HttpResponse(f"Transaction failed: {e}")
        return response
    
class CustomLoginView(LoginView):
    template_name = 'login.html'
    next_page = reverse_lazy('profile')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

@login_required(login_url='login')
def profile(request):
    return render(request, 'profile.html')

@login_required(login_url='login')
def high_balance_accounts(request):
    accounts = Account.objects.with_balance_above(1000)
    return render(request, 'high_balance_accounts.html', {'accounts': accounts})
