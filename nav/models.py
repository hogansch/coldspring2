from django.db import models
from wagtail.core.models import Page
from home.models import HomePage
# Create your models here.

class Navbar(Page):
    template = "nav.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["board_agenda"] = HomePage.objects.first().board_agenda
        # context["district_map"] = 
        return context

    content_panels = Page.content_panels + []
