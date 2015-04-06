# -*- coding: utf-8 -*-
from django.contrib import admin

# Register your models here.
from mytodo.models import *


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'content','order', 'done')


admin.site.register(Todo, TodoAdmin)