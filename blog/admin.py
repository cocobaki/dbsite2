from django.contrib import admin

# Register your models here.

from blog.models import Category, Tag, Post, ContentImage

class ContentImageInline(admin.TabularInline):
    model = ContentImage
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [
        ContentImageInline,
    ]

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm
from .models import CustomUser
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'email', 'last_name', 'first_name', 'is_staff',]
admin.site.register(CustomUser, CustomUserAdmin)