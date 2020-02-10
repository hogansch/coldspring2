from wagtail.core import hooks

from minutes.views import AgendaChooserViewSet


@hooks.register('register_admin_viewset')
def register_person_chooser_viewset():
    return AgendaChooserViewSet('agenda_chooser', url_prefix='agenda-chooser')