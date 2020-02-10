from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from agendas.models import Agenda
from .widgets import AgendaChooser

# Create your models here.
class Minutes(models.Model):
    date = models.DateField(verbose_name="Date of Meeting")
    regular_or_special = models.CharField(max_length=10, choices=[
        ("regular", "Regular session"), ("special", "Special session"), 
        ("notice", "Notice of Public Hearing"), ("canceled", "Cancelled session"),  
    ], null=True, default="general")
    document = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=False,
        on_delete=models.CASCADE,
        related_name='+',
        verbose_name="Minutes PDF"
    )
    assoc_agenda = models.ForeignKey(
        'agendas.Agenda',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Associated Agenda"
    )


    panels = [MultiFieldPanel([
                FieldPanel('date'),
                FieldPanel('regular_or_special'),
            ]),
            DocumentChooserPanel('document'),
            FieldPanel('assoc_agenda', widget=AgendaChooser)
    ]

    def save(self, *args, **kwargs):
        super(Minutes, self).save(*args, **kwargs)

        self.assoc_agenda.assoc_minutes = self
        self.assoc_agenda.save()

    
    def __str__(self):
        return self.document.title    
    
    class Meta:
        verbose_name_plural = "Minutes"
    
        
