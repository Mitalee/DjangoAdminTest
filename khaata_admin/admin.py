from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from .models import SettlementSummary, User


# Register your models here.
class SettlementSummaryAdmin(admin.ModelAdmin):
    list_display = (
        'user_id', 'view_records_link', 'total_num_transactions', 'settlement_id', 'report_id', 'total_amount',
        'start_date', 'end_date', 'deposit_date')
    # list_display_links = ('transaction_id',)
    list_filter = ('user_id', 'settlement_id')

    def get_queryset(self, request):
        query_set = super(SettlementSummaryAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return query_set
        return query_set.filter(user_id=request.user.link_to_user)

    def view_records_link(self, obj):
        url = u'../transaction/?user_id=%d&settlement_id=%s' % (obj.user_id, obj.settlement_id)
        return format_html("<a href='{url}'>View Records</a>", url=url)


class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'link_to_user']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('link_to_user',),
        }),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'classes': ('wide',),
            'fields': ('link_to_user',),
        }),
    )


admin.site.register(SettlementSummary, SettlementSummaryAdmin)
admin.site.register(User, CustomUserAdmin)
