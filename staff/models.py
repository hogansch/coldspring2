from django.db import models
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel
from modelcluster.fields import ParentalKey
from wagtail.core.models import Orderable, Page
from modelcluster.models import ClusterableModel

class StaffCategory(ClusterableModel):
    cat_title = models.CharField(
        max_length=255, 
        blank=False, 
        null=True,
        verbose_name="Staff Category Name"
    )

    panels = [MultiFieldPanel([
            FieldPanel('cat_title'),
            InlinePanel(
                'staff_member', 
                label="Staff Member", 
                heading="Staff Member Info"
            )
        ])
    ]

    def __str__(self):
        return self.cat_title

    class Meta:
        verbose_name_plural = "Categories"

class StaffOrderable(Orderable):
    parent_model = ParentalKey(StaffCategory, on_delete=models.CASCADE, 
        related_name='staff_member', null=True)
    first_name = models.CharField(max_length=100, blank=False, null=True)
    last_name = models.CharField(max_length=100, blank=False, null=True)
    title = models.CharField(max_length=10, choices=[
        ("ms", "Ms."), ("mx", "Mx."), ("mr", "Mr."), ("dr", "Dr.")
    ], null=True)
    grade = models.CharField(
        max_length=100, 
        blank=True, 
        verbose_name="Grade or job title / description",
        help_text="""If the staff member is a teacher, enter a grade (K - 6). 
        Otherwise add a job title or description.""")
    ext = models.CharField(
        max_length=3, 
        blank=False, 
        null=True, 
        verbose_name="Phone extension")
    email = models.EmailField(max_length=100, blank=True)
    cover_photo = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        verbose_name="Photo"
    )

    panels = [
        FieldPanel('first_name'),
        FieldPanel('last_name'),
        FieldPanel('title'),
        FieldPanel('grade'),
        FieldPanel('ext'),
        FieldPanel('email'),
        ImageChooserPanel('cover_photo')
    ]

    def __str__(self):
        return self.first_name + " " + self.last_name

class StaffDirectoryPage(Page):
    template = "staff_directory_page.html"
    submenutitle = models.CharField(max_length=255, null=True,  verbose_name="Submenu title") 

    content_panels = Page.content_panels + [
        FieldPanel('submenutitle')
    ]

    def get_context(self, request, *args, **kwargs):
        context= super().get_context(request, *args, **kwargs)
        sc = StaffCategory.objects.all()
        context["teachers"] = sc[0].staff_member.all()
        context["special"] = sc[1].staff_member.all()
        context["admin"] = sc[2].staff_member.all()
        context["dolphins"] = sc[3].staff_member.all()
        return context


        # note: in order to access individual Staff Categories, use
        # the form staff[i].staff_member.all()
    
    is_creatable = False

# class Classroom(ClusterableModel):

#     cat_title = models.CharField(
#         max_length=255, 
#         blank=False, 
#         null=True,
#         verbose_name="Classroom Category",
#         choices=[
#             ("classrooms","Classrooms"), ("specialists","Specialists")
#         ]
#     )

#     panels = [MultiFieldPanel([
#             FieldPanel('cat_title'),
#             InlinePanel(
#                 'classroom', 
#                 label="Classroom", 
#                 heading="Classroom Info"
#             )
#         ])
#     ]

#     def __str__(self):
#         return self.cat_title

#     class Meta:
#         verbose_name_plural = "Classrooms"

# class ClassroomOrderable(Orderable):
#     parent_model = ParentalKey(ClassroomCategory, on_delete=models.CASCADE, 
#         related_name='classroom', null=True)
#     teacher = 

#     panels = [
#         FieldPanel('first_name'),
#         FieldPanel('last_name'),
#         FieldPanel('title'),
#         FieldPanel('grade'),
#         FieldPanel('ext'),
#         FieldPanel('email'),
#         ImageChooserPanel('cover_photo')
#     ]

#     def __str__(self):
#         return self.first_name + " " + self.last_name


# class ClassroomsPage(Page):
#     template = "classrooms_page.html"
#     submenutitle = models.CharField(max_length=255, null=True,  verbose_name="Submenu title") 

#     content_panels = Page.content_panels + [
#         FieldPanel('submenutitle')
#     ]

#     def get_context(self, request, *args, **kwargs):
#         context= super().get_context(request, *args, **kwargs)
#         sc = StaffCategory.objects.all()
#         context["teachers"] = sc[0].staff_member.all()
#         context["special"] = sc[1].staff_member.all()
#         return context
    
#     # is_creatable = False