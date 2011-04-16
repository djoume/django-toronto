from django import forms
from django.contrib import admin


from profiles.models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    form = UserProfileForm
    list_display = ('name', 'picture', 'description')


admin.site.register(UserProfile, UserProfileAdmin)
