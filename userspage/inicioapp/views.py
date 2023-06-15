from django.views.generic import View, CreateView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy


# Create your views here.


class Home(View):
    def get(self, request):
        return render(request, 'home.html', {})


class Usuarios(View):
    @classmethod
    def is_admin(cls, user):
        return user.is_authenticated and user.is_superuser

    def dispatch(self, request, *args, **kwargs):
        if not self.is_admin(request.user):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        all_users = User.objects.all()
        return render(request, 'usuarios.html', {'users': all_users})


class Registro(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'


class SuSignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/susignup.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.is_superuser = True
        return super().form_valid(form)
