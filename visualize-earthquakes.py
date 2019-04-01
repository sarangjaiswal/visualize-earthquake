# importing library
import folium
import time
import requests
import geopandas as gpd
import os

# get current directory path
cur_dir = os.path.dirname(os.path.realpath(__file__))

# target path to save map
map_path = os.path.join('maps', 'earthquake_india.html')

# read shape files with geopandas
Micro_Plates_and_Major_Fault_Zones = gpd.read_file(cur_dir + '/data/mygeodata/plate-boundaries/shp/Micro_Plates_and_Major_Fault_Zones-line.shp')
Plate_Interface = gpd.read_file(cur_dir + '/data/mygeodata/plate-boundaries/shp/Plate_Interface-line.shp')
Plate_Motion = gpd.read_file(cur_dir + '/data/mygeodata/plate-boundaries/shp/Plate_Motion-point.shp')

# Open the map at a location with a certain zoom start - http://geojson.io/#map=5/22.573/74.751
m = folium.Map(location=[22.573, 74.751], zoom_start=5)

# creating feature groups which will be added to map as layers
fg_zone = folium.FeatureGroup('Micro Plates & Major Fault Zones')
fg_interface = folium.FeatureGroup('Plate Interface')
fg_motion = folium.FeatureGroup('Plate Motion')
fg_earthquake = folium.FeatureGroup('Earthquake Data')

# adding micro plates and major fault zones data to feature group
folium.Choropleth(
    geo_data=Micro_Plates_and_Major_Fault_Zones,
    line_color='red',
    line_weight=2,
    line_opacity=1,
    highlight=True
).add_to(fg_zone)

# adding plate interface data to feature group
folium.Choropleth(
    geo_data=Plate_Interface,
    line_color='red',
    line_weight=2,
    line_opacity=1,
    highlight=True
).add_to(fg_interface)

# adding plate motion data to feature group
folium.GeoJson(Plate_Motion).add_to(fg_motion)

# adding the feature group to folium map
fg_zone.add_to(m)
fg_interface.add_to(m)
fg_motion.add_to(m)

# Read earthquake from past hour
url_1hour = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'
url_1day = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson'
url_7days = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson'
url_30days = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson'
url_history = 'https://earthquake.usgs.gov/fdsnws/event/1/query?format=geojson&minlatitude=3&minlongitude=37&maxlatitude=63&maxlongitude=98&starttime=2010-01-01&endtime=2019-01-02'

r = requests.get(url_history)
data = r.json()

# extracted from https://en.wikipedia.org/wiki/Modified_Mercalli_intensity_scale
color_list = {
    1: '#ffffff',
    2: '#bfccff',
    3: '#99f',
    4: '#8ff',
    5: '#7df894',
    6: '#ff0',
    7: '#fd0',
    8: '#ff9100',
    9: '#f00'
    }

# getting the number of records in json
count = data["metadata"]["count"]

# tool tip text
tooltip = 'Click for more info.'

# iterating all the json records
for i in range(0, count-1):
    title = data["features"][i]["properties"]["title"]
    if title.find("India") != -1:

        # get the magnitude, round to nearest number and convert to int
        mag = int(round(data["features"][i]["properties"]["mag"], 0))

        # convert the time into readable format
        event_time = time.strftime(
                        '%Y-%m-%d %H:%M:%S',
                        time.localtime(round(data["features"][i]["properties"]["time"]/1000, 10))
                    )
        # html format for pop ups
        popup = f"""<div><strong>Place : </strong>{data["features"][i]["properties"]["place"]}</div>
                    <div>
                        <strong>Magnitude : </strong>
                        <div style="background-color:{color_list.get(mag)}">
                            {data["features"][i]["properties"]["mag"]}
                        </div>
                    </div>
                    <div><strong>Date : </strong>{event_time}</div>
                    <div><strong>Type : </strong>{data["features"][i]["properties"]["type"]}</div>
                """
        # get longitude and latitude from json data
        lon = data["features"][i]["geometry"]["coordinates"][0]
        lat = data["features"][i]["geometry"]["coordinates"][1]

        # Add a circles to feature group
        folium.CircleMarker(
            location=[lat, lon],
            radius=5,
            tooltip=tooltip,
            popup=folium.Popup(popup, max_width=1000),
            color=color_list.get(mag),
            fill=True,
            fill_color=color_list.get(mag)
        ).add_to(fg_earthquake)

# add feature group to map
fg_earthquake.add_to(m)


# add layer to map
folium.LayerControl().add_to(m)

# save map to specified location
m.save(map_path)
