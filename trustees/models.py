# subscribers/models.py
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class Trustee(models.Model):
    """A trustee model."""

    full_name = models.CharField(max_length=100, blank=False, null=False, help_text='First and last name')
    position = models.CharField(max_length=100, blank=False, null=False, help_text='Position')
    term_start = models.CharField(max_length=4, blank=False, null=False, help_text='Year that term started')
    term_end = models.CharField(max_length=4, blank=False, null=False, help_text='Year that term ends')

    def __str__(self):
        """Str repr of this object."""
        return self.full_name

    class Meta:  # noqa
        verbose_name = "Trustee"
        verbose_name_plural = "Trustees"
        db_table = "Trustee"

class TrusteesPage(Page):
    template = "trustees_page.html"
    submenutitle = models.CharField(max_length=100, null=True, verbose_name="Submenu title")

    content_panels = Page.content_panels + [
        FieldPanel('submenutitle')
    ]

    def get_context(self, request, *args, **kwargs):
        context= super().get_context(request, *args, **kwargs)
        context["trustees"] = Trustee.objects.all()
        return context
    
    is_creatable = False

   
        
