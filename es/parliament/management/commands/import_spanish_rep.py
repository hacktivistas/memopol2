
# import spanish reps data
#
# TODO: everythin! 
# Create party, regions, parlamentary group, handle the picture well, minor data issues like \r and other chars, etc

from urllib2 import urlopen
import json

from django.core.management.base import BaseCommand

from es.parliament.models import ESParlamentary

class Command(BaseCommand):
    help = 'Import Spain representative data from congreso.es using the scraper wiki script https://scraperwiki.com/scrapers/congreso_datos_diputado/ '

    def handle(self, *args, **options):
        print 'Starting import'
        sw_url = "https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=json&name=congreso_datos_diputado&query=select+*+from+%60swdata%60&apikey="
        json_data = json.loads(urlopen(sw_url).read())
        for rep in json_data:
            self.create_spain_rep(rep)

    def create_spain_rep(self, item):
        representative = {
            "picture": item["url_foto"],
            "first_name": item["nombre"],
            "last_name": item["apellidos"],
            "full_name": "%s %s" % (item["nombre"], item["apellidos"]),
            "ce_estado_civil": item["estado_civil"],
            "ce_cargo": item["cargo"],
            "ce_id": item["id"],
            "id": item["id"],
            "ce_cargos_anteriores": item["cargos_anteriores"],
            "ce_curriculum": item["curriculum"],
            "ce_declaracion_bienes_url": item["declaracion_bienes_url"],
            "ce_declaracion_actividades_url": item["declaracion_actividades_url"],
            "ce_circunscripcion": item["circunscripcion"],
            "ce_legislatura": item["legislatura"],
            "ce_comisiones": item["comisiones"],
            "ce_partido": item["partido"],
            "ce_grupo_parlamentario": item["grupo_parlamentario"],
            # position
            "ce_pos_fila": item["pos_fila"],
            "ce_pos_banca": item["pos_butaca"],
            "ce_pos_sector": item["pos_sector"],
            # social
            "ce_twitter": item["twitter"],
            "ce_facebook_url": item["facebook_url"],
            "ce_web": item["web"],
            "ce_flikr_url": item["flickr_url"],
            "ce_linkedin_url": item["linkedin_url"],
        }
        print representative
        rep = ESParlamentary.objects.get_or_create(id=item["id"], defaults=representative)


# PARTY!!!
#party = Party.objects.get_or_create(name=party)
#PartyRepresentative.create(current=True, representative=rep, party=party) # party! fuck yeah!

