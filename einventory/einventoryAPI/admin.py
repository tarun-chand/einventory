from django.contrib import admin
from einventoryAPI.models import ProductTypeMaster, BuildingMaster, Product_details, User_details, Section_details
# Register your models here.


class ProductTypeMasterAdmin(admin.ModelAdmin):
    list_display = ('product_type_id', 'product_type_name', 'entry_date')


class BuildingMasterAdmin(admin.ModelAdmin):
    list_display = ('building_id', 'building_name', 'entry_date')


class Product_detailsAdmin(admin.ModelAdmin):
    list_display = ('product_id', 'product_type', 'product_name', 'product_model',
                    'product_serialno', 'product_notsheet_no', 'product_price', 'entry_date')


class User_detailsAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name', 'post', 'mobileno', 'entry_date')


class Section_detailsAdmin(admin.ModelAdmin):
    list_display = ('section_id', 'building_name', 'floor',
                    'roomno', 'section_name', 'entry_date')


admin.site.register(ProductTypeMaster, ProductTypeMasterAdmin)
admin.site.register(BuildingMaster, BuildingMasterAdmin)
admin.site.register(Product_details, Product_detailsAdmin)
admin.site.register(User_details, User_detailsAdmin)
admin.site.register(Section_details, Section_detailsAdmin)
