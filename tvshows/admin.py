from django.contrib import admin
from .models import TVShow


# Register your models here.

class TVShowAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return True

    def has_change_permission(self, request, obj=None):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


admin.site.register(TVShow, TVShowAdmin)
