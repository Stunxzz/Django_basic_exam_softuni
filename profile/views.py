from django.forms import PasswordInput
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from profile.models import Profile
from profile.forms import ProfileForm

from car.models import Car


class ProfileCreateView(CreateView):
    model = Profile
    fields = '__all__'
    success_url = reverse_lazy('catalogue')
    template_name = 'profile-create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.save()
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form_class = ProfileForm
        form = super().get_form(form_class)
        exclude_fields = ['first_name', 'last_name', 'profile_picture']
        for field_name in exclude_fields:
            form.fields.pop(field_name)
        return form


class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profile-details.html'
    form_class = ProfileForm
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        profile = Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        cars = Car.objects.all()
        total_price = sum([c.price for c in cars])
        context['total_price'] = total_price
        return context




class ProfileDeleteView(DeleteView):
    model = Profile
    template_name = 'profile-delete.html'
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.object
        return context

    def post(self, request, *args, **kwargs):
        profile = self.get_object()
        profile.delete()
        return HttpResponseRedirect(self.success_url)


class ProfileUpdateView(UpdateView):
    model = Profile
    template_name = 'profile-edit.html'
    form_class = ProfileForm
    success_url = reverse_lazy('catalogue')

    def get_object(self, queryset=None):
        return Profile.objects.first()

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.save()
        return HttpResponseRedirect(self.get_success_url())