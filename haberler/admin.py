from django.contrib import admin
from haberler.models import Offenlage
from leaflet.admin import LeafletGeoAdmin
from django.contrib.sessions.models import Session
# Register your models here.


#admin.site.register(Offenlage) 

@admin.register(Offenlage)
class OffenlageAdmin(LeafletGeoAdmin):
    search_fields=('name','stadt','owner',)
    list_display=['name','stadt','owner']
    list_filter=['stadt']
    readonly_fields = ['owner','typ','planart']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(owner=request.user) 


    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        obj.last_modified_by = request.user
        obj.save() 

   
   