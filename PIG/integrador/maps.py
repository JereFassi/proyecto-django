import logging
import folium
import math

logger = logging.getLogger(__name__)

def generar_mapa_html(localizacion):

    indice = math.floor(len(localizacion) / 2)

    latitud = localizacion[indice]['lat']
    longitud = localizacion[indice]['lon']
    tooltip = localizacion[indice]['display_name']

    mapa = folium.Map(location=[latitud, longitud], zoom_start = 16)

    for i in (range(len(localizacion))):
        latitud = localizacion[i]['lat']
        longitud = localizacion[i]['lon']
        tooltip = localizacion[i]['display_name']

        folium.Marker(
                [latitud, longitud],
                popup = "<i>Geo del Domicilio</i>",
                tooltip = tooltip
        ).add_to(mapa)

    folium.LayerControl().add_to(mapa)
    mapa_html = mapa._repr_html_()

    return mapa_html