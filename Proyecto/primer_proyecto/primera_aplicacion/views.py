from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.models import User

# Create your views here.
def index_welcome(request):
    return render(request, 'welcome.html')

class UsersApp(TemplateView):
    template_name = "users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['usuarios'] = User.objects.all()
        print(context['usuarios'][1].__dict__)
        return context