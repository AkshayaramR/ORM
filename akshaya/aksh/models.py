from django.db import models
from django.contrib import admin
class footballPlayer (models.Model):
    noofplayers=models.IntegerField()
    nameoftheplayer=models.CharField(max_length=10)
    noofteams=models.IntegerField()
    noofgoals=models.IntegerField()

class footballPlayerAdmin(admin.ModelAdmin):
    list_display=('noofplayers','nameoftheplayer','noofteams','noofgoals')
