import folium

copyright_osm = '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'

_map = folium.Map(location=[35.681167, 139.767052],
  attr=copyright_osm,
)

#MarkerをMapping
folium.Marker([35.681167, 139.767052], popup='<i>東京駅</i>').add_to(_map)
folium.Marker([35.697914, 139.413741], popup='<b>立川駅</b>').add_to(_map)

_map.save('sample1.html')
