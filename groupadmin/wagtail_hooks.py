from wagtail.contrib.modeladmin.options import (
    ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import (
    Book, Author, Genre)


class BookAdmin(ModelAdmin):
    model = Book
    menu_label = 'Book'  # ditch this to use verbose_name_plural from model
    menu_icon = 'pilcrow'  # change as required
    list_display = ('title', 'author',)
    list_filter = ('genre', 'author',)
    search_fields = ('title', 'author',)


class AuthorAdmin(ModelAdmin):
    model = Author
    menu_label = 'Author'  # ditch this to use verbose_name_plural from model
    menu_icon = 'user'  # change as required
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class GenreAdmin(ModelAdmin):
    model = Genre
    menu_label = 'Genre'  # ditch this to use verbose_name_plural from model
    menu_icon = 'group'  # change as required
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


class LibraryGroup(ModelAdminGroup):
    menu_label = 'Library'
    menu_icon = 'folder-open-inverse'  # change as required
    menu_order = 200  # will put in 3rd place (000 being 1st, 100 2nd)
    items = (BookAdmin, AuthorAdmin, GenreAdmin)

# When using a ModelAdminGroup class to group several ModelAdmin classes together,
# you only need to register the ModelAdminGroup class with Wagtail:
modeladmin_register(LibraryGroup)