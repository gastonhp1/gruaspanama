from django.contrib import admin
from gruaspanama.models import Maquina

class MaquinaInline(admin.TabularInline):

    model = Maquina
    extra = 0

class MaquinaAdmin(admin.ModelAdmin):
    inlines = [MaquinaInline]

@admin.register(Maquina)
class MaquinaAdmin(admin.ModelAdmin):

    fieldsets = [
        (
            "Datos generales",
            {
                "fields": [
                    'modelo', 'imagen', 'marca' , 'segmento', 'año', 'capacidad', 'pluma', 'plumin', 'potencia', 'disponible'
                ]
            },
        ),

    ]

    list_display = ['modelo', 'año', 'marca', 'segmento', 'capacidad', 'pluma', 'plumin', 'potencia', 'disponible']
    list_filter = ('modelo', 'capacidad', 'potencia')
    search_fields=('modelo', 'marca', 'segmento')

    @admin.display(Maquina)
    def show_modelo(self, obj):
        return ("%s" % (obj.Maquina.modelo).upper())

#admin.site.register(Maquina, MaquinaAdmin)

#admin.site.register(Maquina)

