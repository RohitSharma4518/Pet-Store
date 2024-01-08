from django.contrib import admin
from . models import Pet


# Register your models here.
class PetAdmin(admin.ModelAdmin):
    list_display = [
        "petid",
        "petname",
        "petgender",
        "petage",
        "petdescription",
        "petphoto"
    ]


admin.site.register(Pet, PetAdmin)
