from django.shortcuts import render,redirect,get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Pupil
# Create your views here.


def pupils_list(request):
    if 'pupil' not in request.GET:
        pupils = Pupil.objects.all()
        return render(request,'pupils/pupils_list.html',context={'pupils': pupils})
    else:
        pupils = Pupil.objects.filter(name__contains=request.GET['pupil'])
        return render(request, 'pupils/pupils_list.html', context={'pupils': pupils})


def pupil_detail(request,pk):
    pupil = Pupil.objects.get(id=pk)
    return render(request,'pupils/pupil_info.html',context={'pupil': pupil})


def pupils_create(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        mark_1 = request.POST['mark_1']
        mark_2 = request.POST['mark_2']
        mark_3 = request.POST['mark_3']
        mark_4 = request.POST['mark_4']
        mark_5 = request.POST['mark_5']
        mark_6 = request.POST['mark_6']

        new_pupil = Pupil(name=name,age=age,mark_1=mark_1,mark_2=mark_2,mark_3=mark_3,mark_4=mark_4,mark_5=mark_5,mark_6=mark_6)
        new_pupil.save()
        return redirect('pupil_info',pk=new_pupil.pk)
    else:
        return render(request,'pupils/add_pupil.html')


def pupils_edit(request,pk):
    this_pupil = get_object_or_404(Pupil,id=pk)
    if request.method == "POST":
        this_pupil.name = request.POST['name']
        this_pupil.age = request.POST['age']
        this_pupil.mark_1 = request.POST['mark_1']
        this_pupil.mark_2 = request.POST['mark_2']
        this_pupil.mark_3 = request.POST['mark_3']
        this_pupil.mark_4 = request.POST['mark_4']
        this_pupil.mark_5 = request.POST['mark_5']
        this_pupil.mark_6 = request.POST['mark_6']

        this_pupil.save()
        return redirect('pupil_info',pk=this_pupil.pk)
    else:
        return render(request,'pupils/edit_pupil.html',{'pupil': this_pupil})



def delete_pupil(request, pk):
    delete_pupils = get_object_or_404(Pupil, id=pk)
    if request.method == "POST":
        if 'confirm_delete' in request.POST:
            delete_pupils.delete()
            return redirect('pupils_list')
    else:
        return render(request, 'pupils/delete_pupil.html', {'delete_pupils': delete_pupils})