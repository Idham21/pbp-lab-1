from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_wishlist_xml, name='show_xml'),
    path('json/', show_wishlist_json, name='show_json'),
    path('json/<int:id>', show_wishlist_json_by_id, name='show_json_by_id'),
    path('xml/<int:id>', show_wishlist_xml_by_id, name='show_xml_by_id'),
]