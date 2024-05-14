from django.contrib import admin

from .models import WolfAIContext, DragonAIContext, HedgehogAIContext


class WolfAIContextAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        return not WolfAIContext.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class DragonAIContextAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        return not DragonAIContext.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


class HedgehogAIContextAdmin(admin.ModelAdmin):
    def has_add_permission(self, *args, **kwargs):
        return not HedgehogAIContext.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(WolfAIContext, WolfAIContextAdmin)
admin.site.register(DragonAIContext, DragonAIContextAdmin)
admin.site.register(HedgehogAIContext, HedgehogAIContextAdmin)
