from django.db import models
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from modelcluster.fields import ParentalKey
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, InlinePanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock

class CustomImageChooserBlock(blocks.StructBlock):
    """Image content"""

    image = ImageChooserBlock(required=True)
    bg_color = blocks.ChoiceBlock(required=True, choices=[
        ('white', 'White'),
        ('lightgray', 'Light Gray'),
    ], default='white', label="Background Color")
    image_position = blocks.ChoiceBlock(required=True, choices=[
        ('left', 'Left'),
        ('center', 'Center')
    ], default='center', label="Image Position")
    image_size = blocks.ChoiceBlock(required=True, choices=[
        ('large', 'Large'),
        ('medium', 'Medium')
    ], default='large', label="Image Size")
    class Meta:
        template = "stream/custom_image_chooser_block.html"
        icon = "pilcrow"
        label = "Image"

class CustomRichTextBlock(blocks.StructBlock):
    """Rich text content"""

    richtext_content = blocks.RichTextBlock(required=True, label="Text Content", 
                                            features=['h2','h3','h4','bold','italic',
                                            'hr','link','document-link','center', 
                                            'ol', 'ul', 'font_color'])
    bg_color = blocks.ChoiceBlock(required=True, choices=[
        ('white', 'White'),
        ('lightgray', 'Light Gray'),
    ], default='white', label="Background Color")

    class Meta:
        template = "stream/custom_rich_text_block.html"
        icon = "pilcrow"
        label = "Text"

class ImageTextSideBySideBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    text = blocks.RichTextBlock(required=False)
    bg_color = blocks.ChoiceBlock(required=True, choices=[
        ('white', 'White'),
        ('lightgray', 'LightGray')
    ], default='white', label="Background Color")
    position = blocks.ChoiceBlock(required=True, choices=[
        ('text_on_left', 'Text on Left'),
        ('text_on_right', 'Text on Right'),
    ], default='left', label="Text / Image Positioning")
    vertical_position = blocks.ChoiceBlock(required=True, choices=[
        ('middle', 'Vertically Centered Content Within Section'),
        ('top', 'Content Starts at Top of Section'),
    ], default='center_vertical', label="Content Vertical Orientation")

    class Meta:
        template = "stream/image_text_side_by_side_block.html"
        icon = "image " + "Image / Text Side by Side"
        label = "Image / Text Side by Side"

class ImageTextWrapBlock(blocks.StructBlock):
    image = ImageChooserBlock(required=False)
    text = blocks.RichTextBlock(required=False)
    bg_color = blocks.ChoiceBlock(required=True, choices=[
        ('white', 'White'),
        ('lightgray', 'LightGray')
    ], default='white', label="Background Color")
    position = blocks.ChoiceBlock(required=True, choices=[
        ('image_on_left', 'Image on Left'),
        ('image_on_right', 'Image on Right'),
    ], default='left', label="Text / Image Positioning")

    class Meta:
        template = "stream/image_text_wrap_block.html"
        icon = "image " + "Image with Text Wrap Around"
        label = "Image with Text Wrap Around"


class TextAndImagePage(Page):
    template = "stream/text_and_image_page.html"
    submenutitle = models.CharField(max_length=255, null=True,  verbose_name="Submenu title")
    content = StreamField([
        ("text", CustomRichTextBlock()),
        ("image", CustomImageChooserBlock(icon="image")),
        ("textimagesidebyside", ImageTextSideBySideBlock()),
        ("textimagewrap", ImageTextWrapBlock()),
        ("embedding", EmbedBlock())
    ])

    content_panels = Page.content_panels + [
        FieldPanel('submenutitle'),
        StreamFieldPanel('content')
    ]

class AnnouncementPage(Page):
    template = "stream/announcement_page.html"
    date = models.DateField(verbose_name="Date of Announcement", null=True)
    listing_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content = StreamField([
        ("text", CustomRichTextBlock()),
        ("image", CustomImageChooserBlock(icon="image")),
        ("textimagesidebyside", ImageTextSideBySideBlock()),
        ("textimagewrap", ImageTextWrapBlock())
    ], null=True)

    content_panels = Page.content_panels + [
        FieldPanel('date'),
        ImageChooserPanel('listing_image'),
        StreamFieldPanel('content'),
        InlinePanel('gallery_images', label="Gallery images")

    ]

class AnnouncementPageGalleryImage(Orderable):
    page = ParentalKey(AnnouncementPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class AnnouncementListingPage(Page):
    """Listing page lists all the Blog Detail Pages."""

    template = "stream/announcement_listing_page.html"

    def get_context(self, request, *args, **kwargs):
        """Adding custom stuff to our context."""
        context = super().get_context(request, *args, **kwargs)
        # Get all posts
        all_posts = AnnouncementPage.objects.live().public().order_by('-first_published_at')
        # Paginate all posts by 2 per page
        paginator = Paginator(all_posts, 1)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts
        return context

    is_creatable = False
