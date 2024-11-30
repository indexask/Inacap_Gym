from django.shortcuts import render
from .models import Project
from portfolio.forms import LoginForm,RegisterForm
from django.views.generic import CreateView, FormView
from django.shortcuts import render,redirect
from django.contrib.auth import login

def home(request):
    projects = Project.objects.all()
    return render(request, "home.html", {"projects": projects})


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/Inicio/'
    succes_message = "%(name)s Se ha creado exitosamente!"

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'Register.html'
    success_url = '/Inicio/'
    succes_message = "%(name)s Se ha creado exitosamente!"
    def form_valid(self, form):
        print(len(self.request.POST['rut']))
        request = self.request
        login(request, form.save())
        if request.user.admin:
                return redirect('/Administracion/')
        return redirect('/Inicio/' + str(request.user.id))