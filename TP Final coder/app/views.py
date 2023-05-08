from django.shortcuts import render
from app.models import juegos, Profile, Mensaje
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.

# Index que recibe todos los templates heredados.
def index(request):
    context = {
        'posts': juegos.objects.all() 
    }
    return render(request, 'app/index.html', context)

#Class View que muestra una lista de juegos con la opcion de desplegar mas informacion
class JuegoList(ListView):
    model = juegos

#Class View que miestra mas a detalle los juegos a seleccionar
class JuegoDetail(DetailView):
    model = juegos
    context_object_name = 'juegos'

#Class formulario que permite ingresar datos de un nuevo post de juego
class JuegoCreate(LoginRequiredMixin, CreateView):
    model = juegos
    success_url = reverse_lazy('juego-list')
    fields = ['nombre', 'descripcion', 'imagen']
    
    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)

#Class formulario que permite actualiar/cambiar datos de un post
class JuegoUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = juegos
    success_url = reverse_lazy('juego-list')
    fields = ['nombre', 'descripcion', 'imagen']

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return juegos.objects.filter(publisher=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, 'app/Not_found.html')

#Class que permite borrar un post
class JuegoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = juegos
    success_url = reverse_lazy('juego-list')
    fields = '__all__'

#Class que permite el registro y logeo y deslogeo de un usuario
class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/login'


class Login(LoginView):
    next_page = reverse_lazy('index')
    

class Logout(LogoutView):
    template_name = 'registration/logout.html'


class ProfileUpdate(UpdateView):
    model = Profile
    fields = ['imagen']
    success_url = reverse_lazy('index')

class MensajeCreate(CreateView):
    model = Mensaje
    fields = '__all__'
    success_url = reverse_lazy('mensaje-list')


class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = 'mensajes'
    
    def get_queryset(self):
        return Mensaje.objects.filter(destinatario=self.request.user.id).all()


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Mensaje
    success_url = reverse_lazy('mensaje-list')
    
    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')

        return Mensaje.objects.filter(destinatario=user_id).all()