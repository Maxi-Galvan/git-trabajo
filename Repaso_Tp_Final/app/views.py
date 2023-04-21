from django.shortcuts import render
from app.models import juegos
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# Create your views here.


def index(request):
    Juegos = juegos.objects.all()

    return render(request, 'app/base.html', {'juegos': Juegos})


class JuegoList(ListView):
    model = juegos


class JuegoDetail(DetailView):
    model = juegos
    context_object_name = 'juegos'


class JuegoCreate(LoginRequiredMixin, CreateView):
    model = juegos
    success_url = reverse_lazy('juego-list')
    fields = '__all__'


class JuegoUpdate(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = juegos
    success_url = reverse_lazy('juego-list')
    fields = '__all__'

    def test_func(self):
        user_id = self.request.user.id
        post_id = self.kwargs.get('pk')
        return juegos.objects.filter(publisher=user_id, id=post_id).exists()

    def handle_no_permission(self):
        return render(self.request, 'app/Not_found.html')

class JuegoDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = juegos
    success_url = reverse_lazy('juego-list')
    fields = '__all__'


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = '/login'

class Login(LoginView):
    next_page = reverse_lazy('juego-list')
    

class Logout(LogoutView):
    template_name = 'registration/logout.html'