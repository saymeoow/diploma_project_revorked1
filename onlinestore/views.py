from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView
from django.views.generic.edit import FormMixin
from .models import Company, Sneakers, Comments
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddSneakersForm
from .forms import AddSneakersForm, CommentForm
from django.shortcuts import HttpResponse


class Support(TemplateView):
    template_name = 'support.html'


class FakeUrlComment(TemplateView):
    template_name = 'fake.html'


class SneakersList(ListView):
    model = Sneakers
    template_name = 'list.html'
    context_object_name = 'sneakers'

    def get_queryset(self):
        return Sneakers.objects.filter(available=True)


class SneakersCompany(ListView):
    model = Sneakers
    template_name = 'list.html'
    context_object_name = 'sneakers'

    def get_queryset(self):
        return Sneakers.objects.filter(company__slug=self.kwargs['company_slug'])


class SneakersDetail(DetailView, FormMixin):
    model = Sneakers
    template_name = 'detail.html'
    context_object_name = 'sneakers'
    form_class = CommentForm
    success_url = '/thanks_for_comment'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.comment_model = self.get_object()
        self.object.author = self.request.user
        self.object.save()
        return super().form_valid(form)


class AddSneakersView(FormView):
    form_class = AddSneakersForm
    template_name = 'add_sneakers.html'
    success_url = '/'
    model = Sneakers

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class Search(ListView):
    context_object_name = 'search'
    template_name = 'list.html'

    def get_queryset(self):
        return Sneakers.objects.filter(name__contains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
