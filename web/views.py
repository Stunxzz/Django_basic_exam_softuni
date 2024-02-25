from django.shortcuts import render
from django.views.generic import TemplateView
from profile.models import Profile


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context
