from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate

from django.views.generic import DetailView, ListView
from django.views import View

from .models import User
from .forms import UserForm, SignUpForm


class UserListView(ListView):
    model = User
    paginate_by = 5  # if pagination is desired
    template_name = 'user/index.html'
    context_object_name = 'users'


    # def get_context_data(self, **kwargs):
    #     current_category_id = kwargs.get('category_id')
    #     categories = Category.objects.all()
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = categories
    #     context['current_category_id'] = current_category_id
    #     return context

    def get_queryset(self):
        users = User.objects.all()
        return users

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

# class UserFormCreateView(View):
#     def get(self, request, *args, **kwargs):
#         form = UserForm()
#         return render(request, "user/signup.html", {"form": form})
#
#     def post(self, request, *args, **kwargs):
#         form = UserForm(request.POST)
#         if form.is_valid():  # Если данные корректные, то сохраняем данные формы
#             form.save()
#             return redirect('user-list')  # Редирект на указанный маршрут
#         # Если данные некорректные, то возвращаем человека обратно на страницу с заполненной формой
#         return render(request, 'user/signup.html', {'form': form})

# class UserDetailView(DetailView):
#     model = User
#     template_name = 'users/user_detail.html'
#     pk_url_kwarg = 'id'
#     context_object_name = 'user'


