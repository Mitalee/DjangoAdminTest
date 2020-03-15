from rest_framework import serializers
from .models import SettlementSummary

class SettlementSummarySerializer(serializers.ModelSerializer):

    class Meta:
        model = SettlementSummary
        fields = ['user_id', 
                  'settlement_id', 'report_id',
                  'total_amount', 'total_num_transactions', 
                  'start_date','end_date','deposit_date'
                ]