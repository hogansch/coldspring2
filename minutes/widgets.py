from django.contrib.admin.utils import quote
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from generic_chooser.widgets import AdminChooser

from agendas.models import Agenda



class AgendaChooser(AdminChooser):
    choose_one_text = _('Choose an Agenda')
    model = Agenda
    choose_modal_url_name = 'agenda_chooser:choose'