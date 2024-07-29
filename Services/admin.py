from django.contrib import admin
from .models import (
    Category,
    Overview,
    BasicPackage,
    StandardPackage,
    PremiumPackage,
    Description,
    Question,
    Gallery,
    RatingService
)

admin.site.register(Category)
admin.site.register(Overview)
admin.site.register(BasicPackage)
admin.site.register(StandardPackage)
admin.site.register(PremiumPackage)
admin.site.register(Description)
admin.site.register(Question)
admin.site.register(Gallery)
admin.site.register(RatingService)
