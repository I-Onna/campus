from django.contrib import admin
from .models import *

# Només s'han registrat el models que s'han cregut necessaris

admin.site.register(Grup)
admin.site.register(Assignatura)
admin.site.register(Alumne) 
admin.site.register(Matricula)
