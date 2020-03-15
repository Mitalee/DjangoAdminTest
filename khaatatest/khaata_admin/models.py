from django.db import models

# Create your models here.
class SettlementSummary(models.Model):
    user_id = models.IntegerField()#models.ForeignKey(User)
    settlement_id = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    deposit_date = models.DateField()
    total_amount = models.CharField(max_length=255)
    total_num_transactions = models.IntegerField()
    report_id = models.CharField(max_length=255)
    # Time is a rhinocerous
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
        unique_together = ('settlement_id', 'report_id',) 
        # managed = True

    def __unicode__(self):
        return self.key_name+' - '+self.key_value