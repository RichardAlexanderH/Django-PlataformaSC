from django.contrib import admin
from login.models import Usuario, Nivel, logeados

# Register your models here.
#class NivelAdmin(admin.ModelAdmin):
#    list_display = ('id_nivel','nivel',)

#class UsuarioAdmin(admin.ModelAdmin):
#    list_display = ('nombre', 'apellido',)
#    search_fields = ('nombre','apellido',)
#    list_filter = ('nivel_id',)

admin.site.register(Nivel)
admin.site.register(Usuario)
admin.site.register(logeados)

