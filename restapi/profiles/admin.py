from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'first_name', 'last_name', '_profile', 'is_staff', 'is_superuser','is_active')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

    def _profile(self, obj):
        profile = Profile.objects.get(user=obj.id)
        return profile.get_role_name(profile.role) if profile.role else None


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)