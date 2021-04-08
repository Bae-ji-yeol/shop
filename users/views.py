from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from users.forms import SignupForm


def signup(request):
    """
    회원가입
    """
    context = {}

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('list')
        else:
            context['signupForm'] = form

    else:
        form = SignupForm()
        context['signupForm'] = form

    return render(request, 'users/signup.html', context)