from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages


from django.views.generic import DetailView, ListView
from .forms import SignUpForm
from django.contrib.auth.models import User


class UserListView(ListView):
    model = User
    template_name = 'user/index.html'
    context_object_name = 'users'

    def get_queryset(self):
        users = User.objects.all()
        return users

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы залогинены')
            return redirect('home')
        return render(request, 'user/signup.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


# class UserDetailView(DetailView):
#     model = User
#     template_name = 'users/user_detail.html'
#     pk_url_kwarg = 'id'
#     context_object_name = 'user'


