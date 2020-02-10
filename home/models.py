from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.admin.edit_handlers import (
    FieldPanel,
    MultiFieldPanel,
    InlinePanel,
    StreamFieldPanel,
    PageChooserPanel,
)
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel

class HomePageCarouselImages(Orderable):
    """Between 1 and 6 images for the home page carousel."""

    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [ImageChooserPanel("carousel_image")]


class HomePage(Page):

    board_agenda = models.ForeignKey(
        'wagtaildocs.Document',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Select the active board agenda that the homepage will link to"
    )

    content_panels = Page.content_panels + [
        DocumentChooserPanel('board_agenda'),
        MultiFieldPanel(
            [InlinePanel("carousel_images", max_num=6, min_num=1, label="Image")],
            heading="Carousel Images",
        )
    ]

class SubMenu(Page):
    content_panels = Page.content_panels