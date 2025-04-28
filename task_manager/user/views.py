from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate

from django.views.generic import DetailView, ListView
from django.views import View

from .models import CustomUser
from .forms import UserForm, SignUpForm


class UserListView(ListView):
    model = CustomUser
    paginate_by = 5  # if pagination is desired
    template_name = 'user/index.html'
    context_object_name = 'users'


    def get_queryset(self):
        users = CustomUser.objects.all()
        return users

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})


# class UserDetailView(DetailView):
#     model = User
#     template_name = 'users/user_detail.html'
#     pk_url_kwarg = 'id'
#     context_object_name = 'user'


