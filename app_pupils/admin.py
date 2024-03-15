from django.contrib import admin

from app_pupils.models import Pupil
# Register your models here.

class PupilAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','mark_1','mark_2','mark_3')
    search_fields = ('name',)


admin.site.register(Pupil,PupilAdmin)
