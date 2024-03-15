from django.shortcuts import render,redirect,get_object_or_404

# Create your views here.
from .models import Themes


def themes_list(request):
    if 'themes' not in request.GET:
        themes = Themes.objects.all()
        return render(request,'themes/themes_list.html',context={'themes': themes})
    else:
        themes = Themes.objects.filter(name__contains=request.GET['themes'])
        return render(request,'themes/themes_list.html',context={'themes': themes})


def themes_create(request):
    if request.method == "POST":
        name = request.POST['name']
        new_themes = Themes(name=name)
        new_themes.save()
        return redirect('themes_list')
    else:
        return render(request, 'themes/add_themes.html')



def themes_edit(request,pk):
    this_themes = get_object_or_404(Themes,id=pk)
    if request.method == "POST":
        this_themes.name = request.POST['name']

        this_themes.save()
        return redirect('themes_list')
    else:
        return render(request, 'themes/edit_themes.html', {'themes': this_themes})


def delete_themes(request, pk):
    delete_themes = get_object_or_404(Themes, id=pk)
    if request.method == "POST":
        if 'confirm_delete' in request.POST:
            delete_themes.delete()
            return redirect('themes_list')
    else:
        return render(request, 'themes/delete_themes.html', {'delete_themes': delete_themes})