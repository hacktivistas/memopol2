from django.db import models
from reps.models import Representative, Party

class ESParlamentary(Representative):
    ce_id = models.IntegerField() # ID in congreso.es
    ce_email = models.CharField(max_length=255, null=True)
    ce_estado_civil = models.CharField(max_length=255, null=True)
    ce_cargo = models.CharField(max_length=255, null=True)
    ce_cargos_anteriores = models.CharField(max_length=255, null=True)
    ce_curriculum = models.CharField(max_length=255, null=True)
    ce_declaracion_bienes_url = models.URLField()
    ce_declaracion_actividades_url = models.URLField()
    ce_circunscripcion = models.CharField(max_length=255, null=True)
    ce_legislatura = models.CharField(max_length=255, null=True)
    ce_comisiones = models.CharField(max_length=255, null=True)
    # party - yuhu!!
    ce_partido = models.CharField(max_length=255, null=True)
    ce_grupo_parlamentario = models.CharField(max_length=255, null=True)
    # position
    ce_pos_fila = models.IntegerField(default=None, null=True)
    ce_pos_banca = models.IntegerField(default=None, null=True)
    ce_pos_sector =  models.IntegerField(default=None, null=True)
    # social
    ce_twitter = models.URLField(default=None, null=True)
    ce_facebook_url = models.URLField(default=None, null=True) 
    ce_web = models.URLField(default=None, null=True) 
    ce_flikr_url = models.URLField(default=None, null=True) 
    ce_linkedin_url = models.URLField(default=None, null=True) 

