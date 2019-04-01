# https://earthquake.usgs.gov/fdsnws/event/1/
# https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlatitude=3&minlongitude=37&maxlatitude=63&maxlongitude=98
# https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlatitude=3&minlongitude=37&maxlatitude=63&maxlongitude=98&starttime=2014-01-01&endtime=2019-01-02

import folium

import requests

# Open the map at a location with a certain zoom start - http://geojson.io/#map=5/22.573/74.751
m = folium.Map(location=[22.573, 74.751], zoom_start=5)

# Read earthquake from past hour
url_1hour = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
url_1day = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
url_7days = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
url_30days = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
url_history = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlatitude=3&minlongitude=37&maxlatitude=63&maxlongitude=98&starttime=2010-01-01&endtime=2019-01-02'

r = requests.get(url_history)
data = r.json()


count = data["metadata"]["count"]
print(count)

for i in range(0,count-1):
    title = data["features"][i]["properties"]["title"]
    if title.find("India") != -1:
        print(data["features"][i]["properties"]["title"])
        lon = data["features"][i]["geometry"]["coordinates"][0]
        lat = data["features"][i]["geometry"]["coordinates"][1]
        folium.Marker([lat, lon], popup=data["features"][i]["properties"]["place"]).add_to(m)

m.save('earthquake.html')






