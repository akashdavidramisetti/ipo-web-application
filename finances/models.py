from django.db import models
from patients.models import Patient

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=50,
        choices=[
            ('Paid', 'Paid'),
            ('Pending', 'Pending'),
            ('Overdue', 'Overdue')
        ],
        default='Pending'
    )

    def __str__(self):
        return f"Invoice #{self.id} - {self.patient.first_name} {self.patient.last_name}"



class Company(models.Model):
    name = models.CharField(max_length=255)
    logo_url = models.URLField()

    def __str__(self):
        return self.name

        


class IPO(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    price_band = models.CharField(max_length=50)
    open_date = models.DateField()
    close_date = models.DateField()
    issue_size = models.CharField(max_length=100)
    issue_type = models.CharField(max_length=50)
    listing_date = models.DateField()
    status = models.CharField(max_length=50)
    ipo_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_price = models.DecimalField(max_digits=10, decimal_places=2)
    listing_gain = models.DecimalField(max_digits=5, decimal_places=2)
    current_market_price = models.DecimalField(max_digits=10, decimal_places=2)
    current_return = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.company.name} IPO"
    



class Document(models.Model):
    ipo = models.ForeignKey(IPO, on_delete=models.CASCADE)
    rhp_pdf = models.URLField()
    drhp_pdf = models.URLField()

    def __str__(self):
        return f"Documents for {self.ipo.company.name}"
