from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.http import *
from django.contrib.auth import authenticate
from re24_app.forms import *
from re24_app.models import *
from django.contrib.auth import login as authlogin
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.core.serializers import * 
import json

#------------------------------------------------------
#------------------------------------------------------

# the Table Show Code

@login_required(redirect_field_name='login', login_url='')  
def From (request) :
    opj = STU()
    return render (request, 'S_form.html', {'opj':opj})
#------------------------------------------------------

# Detail's Save procses

@login_required(redirect_field_name='login', login_url='')
def DetailSave(request):
    opj = STU(request.POST or None, request.FILES or None)
    if opj.is_valid():
        opj.save()
        return redirect("TableView")
    else:
        return HttpResponse("NOT SAVE")      
#------------------------------------------------------

# TableView

@login_required(redirect_field_name='login', login_url='')  
def TableView(request):
    opj_MOD = Student.objects.all()
    return render (request, 'S_table.html', {'opj': opj_MOD})
#------------------------------------------------------

# Delete Students Details

@login_required(redirect_field_name='login', login_url='')
def Delete(request, id):
    opj_MOD =  Student.objects.get(id = id)
    opj_MOD.delete()
    return redirect("TableView")   
#------------------------------------------------------

# show The Student Detail

@login_required(redirect_field_name='login', login_url='')
def ShowDetails(request, id):
    opj_MOD =  Student.objects.get(id = id)
    return render (request, 'SD_table.html', {'opj': opj_MOD})    
#------------------------------------------------------

# Edit Student's Details

@login_required(redirect_field_name='login', login_url='')
def Edit(request, id):
    opj_MOD = Student.objects.get(id = id)
    opj= STU(request.POST or None, request.FILES or None, instance=opj_MOD)
    if opj.is_valid():
        opj.save()
        return redirect("ShowDetails")
    return render(request, "S_edit.html", {"opj":opj}) 
@login_required(redirect_field_name='login', login_url='')   
#------------------------------------------------------

# mark_Show

def mark(request, id):
   opj = Mark.objects.filter(student_id = id).values()
   return render (request, 'SDM_table.html', {'opj': opj}) 
#------------------------------------------------------
    
# MRK_Add form(Just Form Only Show )

@login_required(redirect_field_name='login', login_url='')
def MRK_form(request):
    opj = MRK()
    return render(request, 'MRK_form.html', {'opj':opj})

# MRK_Save Proccess
    
@login_required(redirect_field_name='login', login_url='')
def MRK_Save(request):
    opj = MRK(request.POST or None, request.FILES or None)
    if opj.is_valid():
        c = opj.save(commit=False)
        c.creator = (request.user).username
        c.save()
        return redirect("MRK_form")   
#------------------------------------------------------

# login_Page:-

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
    
        if user is not None:
            if user.is_active:
                authlogin(request, user)
                return redirect('TableView')
        else:
            return HttpResponse("Try Again")
    
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
#------------------------------------------------------

# Logout_Page:-

def logouted(request):
    logout(request)
    #return render_to_response('promotions.html')
    
    return redirect('login')
    #return HttpResponse('logout')
#------------------------------------------------------

# Mark_Update

@login_required(redirect_field_name='login', login_url='')
def update(request, id):
    opj_MOD = Mark.objects.get(id = id)
    opj= MRK(request.POST or None, request.FILES or None, instance=opj_MOD)
    if opj.is_valid():
        opj.save()
        ak = opj.save(commit=True)
        ak.updator = (request.user).username
        ak.save()
        #return redirect("update")
        return HttpResponse("Update Success")
    return render(request, "MRK_edit.html", {"opj":opj}) 
#------------------------------------------------------
 
# jason_formate :-
'''def Jason(request):
   opj=list(Mark.objects.values())
   print(type(opj))
   return JsonResponse(opj,safe=False) '''

def Jason(request, pretty=True):
    stu_mark = Mark.objects.all()
    opj = serialize('json', stu_mark, fields=(
        'student',
        'sub',
        'mrk',
        'created_at',
        'updated_at',
        'creator',
        'updator'))
    opj1 = json.dumps(json.loads(opj), indent=4)
    print(type(opj1))
    return HttpResponse(opj1, content_type="application/json")
  


