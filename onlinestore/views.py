from django.views.generic import ListView, DetailView, CreateView, TemplateView, FormView
from .models import Company, Sneakers
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddSneakersForm
from .forms import AddSneakersForm


class Support(TemplateView):
    template_name = 'support.html'


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


class SneakersDetail(DetailView):
    model = Sneakers
    template_name = 'detail.html'
    context_object_name = 'sneakers'


class SneakersDetailView(FormView):
    template_name = 'detail.html'
    form_class = CartAddSneakersForm
    model = Sneakers

    def get_success_url(self):
        return self.request.path

    def get_sneakers(self):
        id = self.kwargs['id']
        slug = self.kwargs['slug']
        return get_object_or_404(Sneakers, id=id, slug=slug, available=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sneakers'] = self.get_sneakers()
        return context

    def form_valid(self, form):
        sneakers = self.get_sneakers()
        return super().form_valid(form)


class AddSneakersView(FormView):
    form_class = AddSneakersForm
    template_name = 'add_sneakers.html'
    success_url = '/'
    model = Sneakers

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
