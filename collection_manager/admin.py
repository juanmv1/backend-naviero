from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import (
    Pais, Puerto, Sector, TipoOperacion, Aduana, TipoCarga, ViaTransporte, RegimenImportacion,
    ModalidadVenta, Region, UnidadMedida, TipoMoneda, Clausula, Ruta
)

# Registrar cada modelo en el panel de administración utilizando SimpleHistoryAdmin
@admin.register(Sector)
class SectorAdmin(SimpleHistoryAdmin):
    list_display = ['id', 'cd_reparticion', 'nombre', 'sitport_valor', 'sitport_nom']
    search_fields = ['nombre', 'sitport_valor', 'sitport_nom']

@admin.register(Pais)
class PaisAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'continente']
    search_fields = ['nombre', 'codigo']

@admin.register(Puerto)
class PuertoAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'pais', 'tipo', 'latitud', 'longitud', 'zona_geografica', 'sector','important', 'eslora_max', 'tipos_cargas']
    search_fields = ['nombre', 'codigo', 'pais__nombre','tipo', 'tipos_cargas']
    list_filter = ['pais', 'sector']
    autocomplete_fields = ['pais', 'sector']

@admin.register(Ruta)
class RutaAdmin(SimpleHistoryAdmin):
    list_display = ['origen', 'destino', 'distancia']
    search_fields = ['origen__nombre', 'origen__codigo', 'destino__nombre', 'destino__codigo']
    list_filter = ['origen__pais', 'destino__pais']
    ordering = ['origen__codigo', 'destino__codigo']
@admin.register(TipoOperacion)
class TipoOperacionAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'ind_ingreso', 'ind_salida']
    search_fields = ['nombre', 'codigo']

@admin.register(Aduana)
class AduanaAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'latitud', 'longitud']
    search_fields = ['nombre', 'codigo']

@admin.register(TipoCarga)
class TipoCargaAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'descripcion']
    search_fields = ['nombre', 'codigo']

@admin.register(ViaTransporte)
class ViaTransporteAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre']
    search_fields = ['nombre', 'codigo']

@admin.register(RegimenImportacion)
class RegimenImportacionAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'sigla', 'active']
    search_fields = ['nombre', 'codigo']
    list_filter = ['active']

@admin.register(ModalidadVenta)
class ModalidadVentaAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'descripcion']
    search_fields = ['nombre', 'codigo']

@admin.register(Region)
class RegionAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre']
    search_fields = ['nombre', 'codigo']

@admin.register(UnidadMedida)
class UnidadMedidaAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'unidad']
    search_fields = ['nombre', 'codigo']

@admin.register(TipoMoneda)
class TipoMonedaAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'pais']
    search_fields = ['nombre', 'codigo']
    list_filter = ['pais']

@admin.register(Clausula)
class ClausulaAdmin(SimpleHistoryAdmin):
    list_display = ['codigo', 'nombre', 'sigla']
    search_fields = ['nombre', 'codigo']
