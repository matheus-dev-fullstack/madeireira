from django.contrib import admin

from termo.models import Equipamento, Termo, Usuario

# Register your models here.

class EquipamentoInline(admin.TabularInline):
    model = Equipamento
    extra = 1
class TermoAdmin(admin.ModelAdmin):
    inlines = [EquipamentoInline]


admin.site.register(Usuario)
admin.site.register(Equipamento)
admin.site.register(Termo)
# admin.site.register(Termo, TermoAdmin)

