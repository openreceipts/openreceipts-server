import uuid
from base64 import b64decode, urlsafe_b64decode

from django.core.files.base import ContentFile
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView
from django.views.generic import ListView
from django.views.generic.detail import SingleObjectTemplateResponseMixin, DetailView, SingleObjectMixin
from django.views.generic.edit import ModelFormMixin
from django.views.generic.edit import ProcessFormView

from .forms import ReceiptScanForm
from .models import ReceiptScan


class CreateUpdateView(SingleObjectTemplateResponseMixin, ModelFormMixin, ProcessFormView):
    def get_object(self, queryset=None):
        try:
            return super(CreateUpdateView, self).get_object(queryset)
        except AttributeError:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(CreateUpdateView, self).post(request, *args, **kwargs)


class ReceiptCreateUpdateView(CreateUpdateView):
    template_name = 'receipt_form.html'
    form_class = ReceiptScanForm
    model = ReceiptScan

    def form_valid(self, form):
        self.object = form.save(commit=False)
        if form.cleaned_data['cropped_image']:
            cropped = form.cleaned_data['cropped_image']
            url_decoded = urlsafe_b64decode(cropped.encode())
            content = ContentFile(url_decoded)
            self.object.image.save('%s.jpg' % str(uuid.uuid4()), content)
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse_lazy('receipt-detail', args=(self.object.id,))


class ReceiptDetailView(DetailView):
    template_name = 'receipt_detail.html'
    model = ReceiptScan


class ReceiptListView(ListView):
    template_name = 'receipt_list.html'
    model = ReceiptScan
    queryset = ReceiptScan.objects.all().order_by('-created')


class ProcessReceiptView(SingleObjectMixin, View):
    model = ReceiptScan

    def post(self, request, pk):
        obj = self.get_object()
        obj.scan_save_result()
        return redirect(reverse_lazy('receipt-detail', args=(obj.id,)))
