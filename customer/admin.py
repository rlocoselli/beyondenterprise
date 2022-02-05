from django.contrib import admin
from customer.models import Client,ClientCategory,ClientType

class CategoryListFilter(admin.SimpleListFilter):
    title = ('Category')
    parameter_name = 'ClientCategory'

    def lookups(self, request, model_admin):
        a = ClientCategory.objects.all()
        
        return list(a.values_list())

    def queryset(self, request, queryset):
    
        if 'ClientCategory' in request.GET.urlencode():
            return queryset.filter(
                client_category=self.value(),
            )
        else:
            return queryset.filter(
            )

class ClientAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'client_category',)
    list_filter = (CategoryListFilter,)

admin.site.register(Client, ClientAdmin)
admin.site.register(ClientCategory)
admin.site.register(ClientType)



