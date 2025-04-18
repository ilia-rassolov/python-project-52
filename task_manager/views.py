from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.shortcuts import redirect


def index(request):
    return render(request, 'index.html', context={
        'who': 'Привет от Хекслета!',
    })

def about(request):
    return render(request, 'about.html')


class HomePageView(TemplateView):

    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['who'] = 'World'
        return context


