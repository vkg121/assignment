
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CountryModel, DocumentSetModel, CustomerModel, CustomerDocumentModel,CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('country',)}),
    )

@admin.register(CountryModel)
class CountryModelAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(DocumentSetModel)
class DocumentSetModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_backside')
    filter_horizontal = ('countries',)

@admin.register(CustomerModel)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'surname', 'nationality', 'gender', 'created_by')

@admin.register(CustomerDocumentModel)
class CustomerDocumentModelAdmin(admin.ModelAdmin):
    list_display = ('customer', 'created_at')
    readonly_fields = ('extracted_json',)

