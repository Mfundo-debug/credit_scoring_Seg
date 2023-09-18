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

# Load the trained model
model = joblib.load('C:/Users/didit/Downloads/Credit scoring and segmentation/credit_scoring_Seg/credit_system/credit_score_app/rfc.joblib')

class CreditScoringPrediction(APIView):
    def post(self, request):
        data = request.data

        # Define a list of required fields
        required_fields = ['age', 'marital_status', 'education_level', 'employment_status',
                           'credit_utilization_ratio', 'payment_history', 'number_of_credit_accounts',
                           'loan_amount', 'interest_rate', 'loan_term', 'type_of_loan']

        # Check if all required fields are present and not empty
        for field in required_fields:
            if field not in data:
                return Response({'error': f'{field} is required'}, status=400)
            if not data[field]:
                return Response({'error': f'{field} cannot be empty'}, status=400)

        # Prepare the input data for prediction
        input_data = {
            'age': float(data.get('age', 0.0)),
            'gender': data.get('gender', ''),
            'marital_status': data.get('marital_status', ''),
            'education_level': data.get('education_level', ''),
            'employment_status': data.get('employment_status', ''),
            'credit_utilization_ratio': float(data.get('credit_utilization_ratio', 0.0)),
            'payment_history': float(data.get('payment_history', 0.0)),
            'number_of_credit_accounts': int(data.get('number_of_credit_accounts', 0)),
            'loan_amount': float(data.get('loan_amount', 0.0)),
            'interest_rate': float(data.get('interest_rate', 0.0)),
            'loan_term': int(data.get('loan_term', 0)),
            'type_of_loan': data.get('type_of_loan', '')
        }

        # Make the prediction
        prediction = model.predict([list(input_data.values())])

        # Return the prediction
        return Response({'prediction': prediction[0]})
