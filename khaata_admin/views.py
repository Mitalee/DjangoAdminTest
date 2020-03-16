from django.shortcuts import render
from rest_framework import viewsets
from .models import SettlementSummary
from .serializers import SettlementSummarySerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SettlementSummaryViewSet(viewsets.ModelViewSet):
    #provides 'list','create','retrieve','update' and 'destroy' actions
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = SettlementSummary.objects.all()
    serializer_class = SettlementSummarySerializer

    def create(self, request, *args, **kwargs):
        # print('DATA: ', request.data)
        # print('SETTLEMENT_ID: ', request.data.get('settlement_id'))
        serializer = self.get_serializer(data=request.data)
        # serializer.is_valid(raise_exception=True) ## DEPRECATED IN FAVOUR OF PRINTING ERRORS
        if not serializer.is_valid():
            print('VALIDATION ERROR: ', serializer.errors)
            # raise ValidationError(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        try:
            self.perform_create(serializer)       
        except Exception as e:
            return Response(str(e), status=status.HTTP_406_NOT_ACCEPTABLE)
        # self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        success_response = "Saved for settlement_ID: "+ request.data.get('settlement_id')
        print(success_response)
        return Response({"success":success_response}, status=status.HTTP_201_CREATED, headers=headers) 