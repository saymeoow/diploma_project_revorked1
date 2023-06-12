from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from django.template.context_processors import csrf
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, FormView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from .models import Profile
from .forms import LoginForm, UserRegistrationForm
from .forms import UserEditForm, ProfileEditForm
User = get_user_model()

# def user_login(request):
#     args = {}
#     args.update(csrf(request))
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(username=cd['username'],
#                                 password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return redirect('/')
#                 else:
#                     args['login_error'] = 'Аккаунт удален'
#                     return render(request, 'login.html', args)
#             else:
#                 args['login_error'] = 'Пользователь не найден'
#                 return render(request, 'login.html', args)
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
#
#
# def logouts(request):
#     auth.logout(request)
#     return redirect('/')


# def register(request):
#     if request.method == 'POST':
#         user_form = UserRegistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             profile = ProfileShow.objects.create(user=new_user)
#             login(request, new_user)
#             return redirect('/')
#     else:
#         user_form = UserRegistrationForm()
#     return render(request, 'register.html', {'user_form': user_form})


class Register(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Логин и пароль не совпадают')
        return super().form_invalid(form)


class Logout(LogoutView):
    success_url = '/'


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect('/auth/profile/')
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request, 'edit_profile.html', {'user_form': user_form},)


class ProfileShow(TemplateView):
    template_name = 'profile.html'


class ProfilePersonal(TemplateView):
    template_name = 'profile_personal.html'


