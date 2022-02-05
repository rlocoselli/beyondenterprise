from django.db import models
from django.utils.translation import gettext_lazy as _


class ClientCategory(models.Model):
    class Meta:
        verbose_name = "Client Industry"
        verbose_name_plural = "Client Industries"

    category_name = models.CharField(max_length=50, verbose_name="Category Name")

    def __str__(self):
        return self.category_name

class ClientType(models.Model):
    client_type = models.CharField(max_length=50, verbose_name="Client Type")

    def __str__(self):
        return self.client_type
        
class Client(models.Model):
    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = _("customers")

    company_name = models.CharField(max_length=100, verbose_name=_("Company Name"))
    first_name = models.CharField(max_length=100, verbose_name="Main contact First Name")
    last_name = models.CharField(max_length=100, verbose_name="Main Contact Last Name")
    client_category = models.ForeignKey(ClientCategory, on_delete=models.CASCADE, verbose_name="Industry")
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE, verbose_name="Type", null = True)

    def __str__(self):
        return self.company_name

class ClientTelephone(models.Model):
    class Meta:
        verbose_name = "Client Telephone"
        verbose_name_plural = "Client Telephones"

    telephone_number = models.CharField(max_length=50, verbose_name="Telephone Number", null = True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Client", null = True)

    def __str__(self):
        return self.telephone_number
