from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.forms import modelformset_factory

from . import models


class PatientDetailView(DetailView):
    model = models.Patient


class PatientListView(ListView):
    model = models.Patient
    context_object_name = 'patients'


class PatientCreateView(CreateView):
    model = models.Patient
    fields = ['lastname', 'firstname']

    def form_valid(self, form):

        # form.instance.author = self.request.user

        return super().form_valid(form)


class PatientUpdateView(UpdateView):
    model = models.Patient
    fields = ['firstname', 'lastname']


class MeasureDetailView(DetailView):
    model = models.Patient


class MeasureListView(ListView):
    model = models.Patient


class MeasureCreateView(CreateView):
    model = models.Measure
    fields = ['name', 'unit']


class PatientMeasureCreateView(CreateView):
    model = models.PatientMeasure
    fields = ['name', 'quantity', 'unit']


class PatientMeasureListView(ListView):
    model = models.PatientMeasure


class MeasureUpdateView(UpdateView):
    model = models.Measure
    fields = ['name', 'quantity', 'unit']


class MeasureDeleteView(DeleteView):
    model = models.Measure
    success_url = reverse_lazy('recipes-home')


class UnitDetailView(DetailView):
    model = models.Unit


class UnitCreateView(CreateView):
    model = models.Unit
    fields = ['name']
    template_name_suffix = '_create_form'

    def get_success_url(self):

        return reverse_lazy('unit-detail', kwargs={'pk': self.object.pk})


class UnitUpdateView(UpdateView):
    model = models.Unit
    fields = ['name']
    template_name_suffix = '_update_form'

    def get_success_url(self):

        return reverse_lazy('unit-detail', kwargs={'pk': self.object.pk})


class UnitListView(ListView):
    model = models.Unit


class UnitDeleteView(DeleteView):
    model = models.Unit
    success_url = 'patient-care-home'
