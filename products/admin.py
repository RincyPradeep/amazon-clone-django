from django.contrib import admin
from products.models import Product,Gallery,Category,Banner,Review
 
 
class GalleryAdmin(admin.TabularInline):
    list_display = ["id","product","image"]
    model = Gallery


class ProductAdmin(admin.ModelAdmin):
    list_display = ["id","title","category","price","is_available"]

    inlines = [GalleryAdmin]
 
admin.site.register(Product,ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id","user","product","rate","created_at"]
 
admin.site.register(Review,ReviewAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id","name"]
 
admin.site.register(Category,CategoryAdmin)


class BannerAdmin(admin.ModelAdmin):
    list_display = ["id","image"]
 
admin.site.register(Banner,BannerAdmin)
