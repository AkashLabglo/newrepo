
from django.contrib import admin
from django.urls import path
from re24_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('from', From, name = 'From'), 
    path('DetailSave', DetailSave, name = 'DetailSave'), 
    path('TableView', TableView, name  = 'TableView'), 
    path('Delete/<id>', Delete, name = 'Delete'), 
    path('ShowDetails/<id>',ShowDetails, name = 'ShowDetails'), 
    path('Edit/<id>', Edit, name = "Edit"), 
    # MRK Paths..
    path("Mark/<id>", mark, name = "Mark"), 
    path('MRK_form', MRK_form, name = 'MRK_form' ),
    path('MRK_Save', MRK_Save, name = 'MRK_save' ), 
    path('Mark/update/<id>', update, name = "update"), 
    # Login_Path
    path("", login, name = "login"), 
    path("logouted", logouted, name = "logouted"),
    # Jason_Paths
    path('Jason', Jason, name = "Jason"),
]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)