from django.urls import path
from haberler.api import views as api_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    

    path('offenlagen/', api_views.offenlage_list_create_api_view, name='offenlagen-list'),
    path('offenlagen/<pk>', api_views.offenlage_list_detail_api_view, name='offenlagen-list'),   
    path('offenlagen/public/', api_views.offenlage_list_published_api_view, name='offenlagen-list'),    
   

 
]

urlpatterns += staticfiles_urlpatterns()