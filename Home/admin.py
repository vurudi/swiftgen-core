# admin.py
from django.contrib import admin
from .models import UserProfile, Skill, Certification, Language, RatingSeller

admin.site.register(UserProfile)
admin.site.register(Skill)
admin.site.register(Certification)
admin.site.register(Language)
admin.site.register(RatingSeller)
