
# import spanish reps data
#
# TODO: everythin! 
# Create party, regions, parlamentary group, handle the picture well, minor data issues like \r and other chars, etc

import urllib2 
import json
import unicodedata

from django.core.management.base import BaseCommand

from es.parliament.models import ESParlamentary


class Command(BaseCommand):
    help = 'Import Spain representative data from congreso.es using the scraper wiki script https://scraperwiki.com/scrapers/congreso_datos_diputado/ '

    def handle(self, *args, **options):
        print 'Starting import'
        sw_url = "https://api.scraperwiki.com/api/1.0/datastore/sqlite?format=json&name=congreso_datos_diputado&query=select+*+from+%60swdata%60&apikey="
        json_data = json.loads(urllib2.urlopen(sw_url).read())
        for rep in json_data:
            self.create_spain_rep(rep)

    def download_picture(self, pk, url):
	filename = 'es/parliament/medias/img/esparlamentary/' + str(pk) + '.jpg'
        try:
            fh = open(filename)
	except IOError:
            img = urllib2.urlopen(url)
            output = open(filename,'wb')
            output.write(img.read())
            output.close()

    def to_ascii(self, s):
        return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    
    def create_spain_rep(self, item):
	# FIXME: id in the URL
        rep_id = self.to_ascii(item["nombre"].strip().replace(' ','')+item["apellidos"].strip().replace(' ',''))
        representative = {
            "picture": item["url_foto"],
            "first_name": item["nombre"].strip(),
            "last_name": item["apellidos"].strip().upper(),
            "full_name": "%s %s" % (item["nombre"].strip(), item["apellidos"].strip().upper()),
            "ce_estado_civil": item["estado_civil"],
            "ce_cargo": item["cargo"],
            "ce_id": item["id"],
            "id": rep_id, 
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
	self.download_picture(item["id"], item["url_foto"])


# PARTY!!!
#party = Party.objects.get_or_create(name=party)
#PartyRepresentative.create(current=True, representative=rep, party=party) # party! fuck yeah!

