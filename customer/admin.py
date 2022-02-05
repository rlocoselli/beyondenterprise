from django.contrib import admin
from customer.models import Client,ClientCategory,ClientType, ClientTelephone

class telephone_inline(admin.TabularInline):
    model = ClientTelephone
    extra = 1

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
    list_editable = ('client_category', )
    list_filter = ('company_name',)
    search_fields = ('company_name',)
    inlines = [telephone_inline, ]

class ClientCategoryAdmin(admin.ModelAdmin):
    list_display = ('id','category_name', )
    list_editable = ('category_name', )

admin.site.register(Client, ClientAdmin)
admin.site.register(ClientCategory, ClientCategoryAdmin)
admin.site.register(ClientType)



