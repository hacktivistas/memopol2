
import datetime
from django.views.generic import DetailView, ListView
from es.parliament.models import ESParlamentary

class ESParlamentaryView(DetailView):
    #queryset=ESParlamentary.objects.all()
    #context_object_name="esparlamentary"
    model = ESParlamentary

    def get_context_data(self, *args, **kwargs):
        context = super(ESParlamentaryView, self).get_context_data(**kwargs)
        context['now'] = datetime.date.today()
        #context['mep'].delegationroles = context['mep'].delegationrole_set.all().select_related('delegation')
        #context['mep'].committeeroles = context['mep'].committeerole_set.all().select_related('committee')
        #context['mep'].opinionreps = context['mep'].opinionrep_set.all().select_related('opinion')
        #context['mep'].scores = context['mep'].score_set.all().select_related('proposal')
        return context
