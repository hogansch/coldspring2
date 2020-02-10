from django.db import models
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import MultiFieldPanel, FieldPanel

class MapPage(Page):
    template = "map_page.html"
    submenutitle = models.CharField(
        max_length=255, 
        null=True,  
        verbose_name="Submenu title"
    )
    top_text = RichTextField(features=[
        'h2','h3','h4','bold','italic',
        'hr','link','document-link','center', 
        'ol', 'ul', 'font_color'
    ])
    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('submenutitle'),
            FieldPanel('top_text')
        ])
    ]