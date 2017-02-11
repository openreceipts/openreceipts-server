from django.contrib import admin

from .models import ReceiptScan


# Register your models here.


class ReceiptScanAdmin(admin.ModelAdmin):
    list_display = ('image', 'raw', 'full_text', 'created', 'modified')
    list_filter = ('created',)
    pass


admin.site.register(ReceiptScan, ReceiptScanAdmin)
