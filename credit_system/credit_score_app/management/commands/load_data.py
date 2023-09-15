import csv
from django.core.management.base import BaseCommand, CommandParser
from credit_score_app.models import Customer

class Command(BaseCommand):
    help = 'Load data from csv file to database'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('csv_file', type=str, help='Path to the CSV file')

    def handle(self, *args, **options):
        csv_file = options['csv_file']
        try:
            with open(csv_file) as f:
                reader = csv.DictReader(f)
                for row in reader:
                    customer = Customer(
                        age=row['Age'],
                        gender=row['Gender'],
                        marital_status=row['Marital Status'],
                        education_level=row['Education Level'],
                        employment_status=row['Employment Status'],
                        credit_utilization_ratio=row['Credit Utilization Ratio'],
                        payment_history=row['Payment History'],
                        number_of_credit_accounts=row['Number of Credit Accounts'],
                        loan_amount=row['Loan Amount'],
                        interest_rate=row['Interest Rate'],
                        loan_term=row['Loan Term'],
                        type_of_loan=row['Type of Loan']
                    )
                    customer.save()
                self.stdout.write(self.style.SUCCESS('Data loaded successfully'))
        except FileNotFoundError:
            self.stderr.write(self.style.ERROR('File not found'))
        except Exception as e:
            self.stderr.write(self.style.ERROR(str(e)))