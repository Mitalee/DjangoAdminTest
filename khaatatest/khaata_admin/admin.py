from django.contrib import admin
from .models import SettlementSummary
from django.utils.html import format_html

# Register your models here.
class SettlementSummaryAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(SettlementSummaryAdmin, self).get_queryset(request)
        user_id = request.user.id
        if request.user.is_superuser:
            return qs
        else:
            return qs.filter(user_id=request.user.id)
    list_display = ('user_id', 'view_records_link', 'total_num_transactions', 'settlement_id','report_id','total_amount','start_date','end_date','deposit_date')
    # list_display_links = ('transaction_id',)
    list_filter = ('user_id','settlement_id')

    def view_records_link(self, obj):
        url = u'../transaction/?user_id=%d&settlement_id=%s' % (obj.user_id, obj.settlement_id)
        return format_html("<a href='{url}'>View Records</a>", url=url)

admin.site.register(SettlementSummary, SettlementSummaryAdmin)