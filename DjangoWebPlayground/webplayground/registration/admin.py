from django.contrib import admin
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user',)
    # Inyectamos nuestro fichero css
    class Media:
        css = {
            'all': ('resgistration/css/custom_ckeditor.css',)
        }
admin.site.register(Profile, ProfileAdmin)
