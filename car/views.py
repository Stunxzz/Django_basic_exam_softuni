from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DetailView, DeleteView, UpdateView
from profile.models import Profile
from car.models import Car
from car.forms import CarForm


class CatalogView(TemplateView):
    template_name = 'catalogue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['cars'] = Car.objects.all()
        return context


class CarCreateView(CreateView):
    model = Car
    fields = '__all__'
    success_url = reverse_lazy('catalogue')
    template_name = 'car-create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()

        return context

    def form_valid(self, form):
        car = form.save(commit=False)
        car.owner = Profile.objects.first()
        car.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form_class = CarForm
        form = super().get_form(form_class)
        return form


class CarDetailView(DetailView):
    model = Car
    template_name = 'car-details.html'
    context_object_name = 'car'

    def get_object(self, queryset=None):
        car_id = self.kwargs.get('pk')
        return Car.objects.get(pk=car_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['car'] = self.object
        return context


class CarDeleteView(DeleteView):
    model = Car
    template_name = 'car-delete.html'
    form_class = CarForm
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        car_id = self.kwargs.get('pk')
        return Car.objects.get(pk=car_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['car'] = self.object
        context['form'] = self.form_class(instance=self.object)  # Подаване на инстанция на формата към контекста
        return context

    def post(self, request, *args, **kwargs):
        car = self.get_object()
        car.delete()
        return HttpResponseRedirect(self.success_url)


class CarUpdateView(UpdateView):
    model = Car
    template_name = 'car-edit.html'
    form_class = CarForm
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        car_id = self.kwargs.get('pk')
        return Car.objects.get(pk=car_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        context['car'] = self.object
        context['form'] = self.form_class(instance=self.object)  # Подаване на инстанция на формата към контекста
        return context

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

