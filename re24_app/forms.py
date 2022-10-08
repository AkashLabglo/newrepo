from re24_app.models import * 
from django.forms import  *


class MRK(ModelForm):
    class Meta:
        model = Mark
        fields = ['student', 'sub', 'mrk']

class STU(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"        
