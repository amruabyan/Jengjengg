import folium
import streamlit as st

from streamlit_folium import st_folium

# center on Liberty Bell, add marker
m = folium.Map(location=[-6.167712327624266, 106.82403602764425], zoom_start=16)
folium.Marker(
    [-6.167712327624266, 106.82403602764425], popup="Our Home", tooltip="Our Home"
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width=725)

{
  "last_clicked": null,
  "last_object_clicked": null,
  "all_drawings": null,
  "last_active_drawing": null,
  "bounds": {
    "_southWest": {
      "lat": 39.90881451094423,
      "lng": -75.17995834350587
    },
    "_northEast": {
      "lat": 39.95488549657055,
      "lng": -75.11773109436037
    }
  },
  "zoom": 14,
  "last_circle_radius": null,
  "last_circle_polygon": null,
  "center": {
    "lat": 39.93187033388333,
    "lng": -75.14888763427736
  }
}