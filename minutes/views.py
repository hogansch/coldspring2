from django.shortcuts import render
from django.utils.translation import ugettext_lazy as _

from generic_chooser.views import ModelChooserViewSet
from agendas.models import Agenda


class AgendaChooserViewSet(ModelChooserViewSet):
    icon = 'pilcrow'
    model = Agenda
    page_title = _("Choose an Agenda")
    per_page = 10
    order_by = 'date'
    fields = ['date', 'regular_or_special']

# Create your views here.
