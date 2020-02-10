from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Trustee


class TrusteeAdmin(ModelAdmin):
    """Trustee admin."""

    model = Trustee
    menu_label = "Trustees"
    menu_icon = "user"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("full_name", "position", "term_start", "term_end")
    search_fields = ("full_name", "position", "term_start", "term_end")

modeladmin_register(TrusteeAdmin)

