from statistics import mode
from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.forms.widgets import OSMWidget
from django.urls import reverse
from django.contrib.gis.geos import GEOSGeometry
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.


class Offenlage(models.Model):

    id = models.AutoField(primary_key=True)
    uuid = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    title = models.CharField(max_length=300, null=True, blank=True)

    createdate = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    changedate = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    lastchanged = models.DateTimeField(auto_now=True, null=True, blank=True)

    offenlage_url = models.CharField(max_length=300, null=True, blank=True)
    owner = models.CharField(max_length=300, null=True, blank=True)
    #owner = models.ForeignKey(User, null=True, blank=True,on_delete=models.CASCADE)
  
    gkz = models.CharField(max_length=300, null=True, blank=True)
    stadt = models.CharField(max_length=300, null=True, blank=True)
    planart  = models.IntegerField( null=True, blank=True)
    rechtsstand  = models.IntegerField(null=True, blank=True)
    offenlage_beginn = models.CharField(max_length=300, null=True, blank=True)
    offenlage_ende = models.CharField(max_length=300, null=True, blank=True)
    kontakt = models.CharField(max_length=2048, null=True, blank=True)
    notiz = models.CharField(max_length=2048, null=True, blank=True)
    public = models.BooleanField(default=True, null=True, blank=True)
    the_geom= models.MultiPolygonField(srid=4326,null=True,blank=True)
    #the_geom2= models.GEOSGeometry(the_geom)
    the_geom_geojson= models.TextField( null=True, blank=True) 
    typ_planart = models.CharField(max_length=300, null=True, blank=True)
    typ = models.CharField(max_length=30, null=True, blank=True)
    offenlage_bekanntmachung = models.CharField(max_length=300, null=True, blank=True)
    uvp_vorpruefung = models.BooleanField(default=True, null=True, blank=True)
    uvp = models.BooleanField(default=True, null=True, blank=True)
    uvp_beginn = models.CharField(max_length=300, null=True, blank=True)
    uvp_ende = models.CharField(max_length=300, null=True, blank=True)
    uvp_kosten = models.FloatField(null=True, blank=True)
    uvp_url = models.CharField(max_length=2048, null=True, blank=True)
    
    def __str__(self):
        return  self.name


