from django.shortcuts import render
from rest_framework import viewsets
from .models import Customer
from .serializers import CustomerSerializer
import joblib
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
#load the trained model

model =joblib.load('C:/Users/didit/Downloads/Credit scoring and segmentation/credit_scoring_Seg/credit_system/credit_score_app/rfc.joblib')
class CreditScoringPrediction(APIView):
    def post(self, request):
        data = request.data
        # Prepare the input data for prediction
        # Make sure the data keys match the features expected by the model
        input_data = {
            #fields from `models.py` here
            'age': float(data.get('age')),
            'gender': data.get('gender'),
            'marital_status': data.get('marital_status'),
            'education_level': data.get('education_level'),
            'employment_status': data.get('employment_status'),
            'credit_utilization_ratio': float(data.get('credit_utilization_ratio')),
            'payment_history': float(data.get('payment_history')),
            'number_of_credit_accounts': float(data.get('number_of_credit_accounts')),
            'loan_amount': float(data.get('loan_amount')),
            'interest_rate': float(data.get('interest_rate')),
            'loan_term': float(data.get('loan_term')),
            'type_of_loan': data.get('type_of_loan')
        }

        #make the prediction
        prediction = model.predict([list(input_data.values())])
        #return the prediction
        return Response({'prediction': prediction[0]})