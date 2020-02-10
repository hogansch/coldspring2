from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.core.models import Page
# from .widgets import AgendaChooser

class Agenda(models.Model):
    date = models.DateField(verbose_name="Date of Meeting")
    regular_or_special = models.CharField(max_length=10, choices=[
        ("regular", "Regular session"), ("special", "Special session"), 
        ("notice", "Notice of Public Hearing"), ("canceled", "Cancelled session"), 
    ], null=True, default="regular", verbose_name="Agenda type")
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name="Agenda PDF"
    )
    assoc_minutes = models.ForeignKey(
        'minutes.Minutes',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Associated minutes (Not required at time Agenda is created)"
    )

    panels = [MultiFieldPanel([
                FieldPanel('date'),
                FieldPanel('regular_or_special'),
            ]),
            DocumentChooserPanel('document'),
    ]

    def __str__(self):
        # return self.date.strftime("%B %d, %Y ") + (
        #     "Board Agenda " +
        #     self.general_or_special + 
        #     " session")
        return self.document.title

class AgendasAndMinutesPage(Page):
    template = "agendas_and_minutes_page.html"
    submenutitle = models.CharField(max_length=100, null=True, verbose_name="Submenu title")
    content_panels = Page.content_panels + [
        FieldPanel("submenutitle")
    ]
    agendas = Agenda.objects.all().order_by('-date')