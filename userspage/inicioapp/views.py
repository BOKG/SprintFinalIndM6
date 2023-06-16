from django.views.generic import View, CreateView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy


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


class EditarUsuario(View):
    def get(self, request, usuario_id):
        usuario = get_object_or_404(User, id=usuario_id)
        form = UserChangeForm(instance=usuario)
        return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})

    def post(self, request, usuario_id):
        usuario = get_object_or_404(User, id=usuario_id)
        form = UserChangeForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()  # Guardar los cambios en el usuario
            # Redirigir a la página de usuarios o a donde desees
            return redirect('usuarios')
        return render(request, 'editar_usuario.html', {'form': form, 'usuario': usuario})


class Registro(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        grupo = self.request.POST.get('grupo')
        if grupo == 'soporte':
            group = Group.objects.get(name='Soporte')
            self.object.groups.add(group)
        elif grupo == 'viewers':
            group = Group.objects.get(name='viewers')
            self.object.groups.add(group)
        login(self.request, self.object)
        return response


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
