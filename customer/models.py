from django.db import models

class ClientCategory(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Category Name")

    def __str__(self):
        return self.category_name

class ClientType(models.Model):
    client_type = models.CharField(max_length=50, verbose_name="Client Type")

    def __str__(self):
        return self.client_type

class Client(models.Model):
    company_name = models.CharField(max_length=100, verbose_name="Company Name")
    first_name = models.CharField(max_length=100, verbose_name="Main contact First Name")
    last_name = models.CharField(max_length=100, verbose_name="Main Contact Last Name")
    client_category = models.ForeignKey(ClientCategory, on_delete=models.CASCADE, verbose_name="Industry")
    client_type = models.ForeignKey(ClientType, on_delete=models.CASCADE, verbose_name="Type", null = True)

    def __str__(self):
        return self.company_name
