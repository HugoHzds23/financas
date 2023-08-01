from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Category, User, Revenue

admin.site.register(User, UserAdmin)


class BaseOwnerAdmin(admin.ModelAdmin):
    """
    Base admin class owned for users.
    """

    def save_model(self, request, obj, form, change):
        """
        Given a model changes the owner to save it.
        """
        obj.owner = request.user
        super().save_model(request, obj, form, change)

    def get_queryset(self, request):
        """
        Return a QuerySet of all model instances created by logged user that can be edited by the
        admin site. This is used by changelist_view.
        """
        qs = super().get_queryset(request)
        return qs.filter(owner=request.user)
    

@admin.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    list_display = ['name', 'created_at', 'updated_at']
    search_fields = ['name']


@admin.register(Revenue)
class RevenueAdmin(BaseOwnerAdmin):
    list_display =  ['description','value','expired_at','payed_at','created_at','updated_at']
    search_fields = ['description','value','expired_at',]