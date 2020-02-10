from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField

class Holiday(models.Model):
    date = models.DateField(verbose_name="Date of Holiday")
    name = models.CharField(max_length=100, null=True, verbose_name="Name of holiday")

    panels = [MultiFieldPanel([
                FieldPanel('date'),
                FieldPanel('name'),
            ]),
    ]

    def __str__(self):
        return self.name

class HolidaysPage(Page):
    template = "holidays_page.html"
    submenutitle = models.CharField(max_length=255, null=True,  verbose_name="Submenu title")
    top_heading = models.CharField(max_length=255, null=True, verbose_name="Heading above table")
    
    bottom_text = RichTextField(features=[
        'h2','h3','h4','bold','italic',
        'hr','link','document-link','center', 
        'ol', 'ul', 'font_color'], verbose_name="Bottom additional text", null=True)
    # def get_context(self, request, *args, **kwargs):
    holidays = Holiday.objects.all().order_by('-date')
    content_panels = Page.content_panels + [
        FieldPanel("submenutitle"),
        FieldPanel("top_heading"),
        FieldPanel("bottom_text")
    ]