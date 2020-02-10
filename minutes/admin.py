from django.contrib import admin
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Minutes

# Register your models here.
class MinutesAdmin(ModelAdmin):
    model = Minutes
    menu_label = 'Minutes'  # ditch this to use verbose_name_plural from model
    menu_icon = 'doc-full'  # change as required
    menu_order = 2  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('date', 'regular_or_special',)
    list_filter = ('date', 'regular_or_special',)
    search_fields = ('date', 'regular_or_special',)

modeladmin_register(MinutesAdmin)
