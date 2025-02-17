from django.contrib import admin

from .models import (
    WolfProduct,
    DragonProduct,
    HedgehogProduct,
    ChickenProduct,
    EggProduct,
)

admin.site.register(WolfProduct)
admin.site.register(DragonProduct)
admin.site.register(HedgehogProduct)
admin.site.register(ChickenProduct)
admin.site.register(EggProduct)
