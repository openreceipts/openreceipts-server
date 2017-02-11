from django.urls import reverse_lazy

__author__ = 'Gokcen'
from django.views.generic import RedirectView
#from django.contrib.auth.decorators import login_required
from django.conf.urls import url

from .views import ReceiptCreateUpdateView, ReceiptDetailView, ProcessReceiptView, ReceiptListView

urlpatterns = [
    url(r'^receipts/$', ReceiptListView.as_view(), name='receipt-list'),
    url(r'^receipts/create$', ReceiptCreateUpdateView.as_view(), name='receipt-create'),
    url(r'^receipts/(?P<pk>[0-9]+)/edit$', ReceiptCreateUpdateView.as_view(), name='receipt-edit'),
    url(r'^receipts/(?P<pk>[0-9]+)/detail$', ReceiptDetailView.as_view(), name='receipt-detail'),

    url(r'^receipts/(?P<pk>[0-9]+)/process$', ProcessReceiptView.as_view(), name='receipt-process'),

    url(r'^$', RedirectView.as_view(url=reverse_lazy('receipt-list')))
]
