from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

def generate_tokens(modeladmin, request, queryset):
    for user in queryset:
        tokens = get_tokens_for_user(user)
        modeladmin.message_user(request, f"Tokens for user {user.username}: Access Token: {tokens['access']}, Refresh Token: {tokens['refresh']}", level='INFO')

generate_tokens.short_description = "Generate Tokens for selected users"


class CustomUserAdmin(UserAdmin):
    actions = [generate_tokens]
    list_display = UserAdmin.list_display + ('get_access_token',)

    def get_access_token(self, obj):
        tokens = get_tokens_for_user(obj)
        return tokens['access']

    get_access_token.short_description = 'Access Token'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)