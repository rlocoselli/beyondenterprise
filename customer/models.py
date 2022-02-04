from django.db import models

class ClientCategory(models.Model):
    category_name = models.CharField(max_length=50, verbose_name="Category Name")

    def __str__(self):
        return self.category_name

class Client(models.Model):
    first_name = models.CharField(max_length=100, verbose_name="First Name")
    last_name = models.CharField(max_length=100, verbose_name="Last Name")
    client_category = models.ForeignKey(ClientCategory, on_delete=models.CASCADE, verbose_name="Category")

    def __str__(self):
        return self.first_name + " " + self.last_name
