# Visualize earthquake's on Indian Sub Continent between 2010 to 2019
A Project to Visualize history of earthquake's on Indian Sub Continent on Map. 

## Installation

This is a **Python 3.6** module that depends on the **Folium** packages.

1. Clone and `cd` into this repo.
2. Install **Python 3.6**.
3. Install requirements from pip with `python3 -m pip install -r requirements.txt`.
4. Test the program by running `visualize-earthquake.py` 

## Usage
Just run `visualize-earthquake.py` file. The output will be a html file `earthquake_india.html` under `\maps` folder. 

Information on GeoJSON Detail Format can be found [here](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson_detail.php)

## Data
All data used in this example is sourced from below websites.
* **USGS**
    * https://earthquake.usgs.gov/
* **Mygeodata**
    * https://mygeodata.cloud/r
* **Shape files**
    * https://github.com/fraxen/tectonicplates

## Map

#### Version 2.0
This is upgraded version of my previous attempt to visualize the earthquakes in Indian Sub-Continent. I have added the following to make it user friendly
* **Added four layers to the visualization**
    * Micro Plates & Major Fault Zones
    * Plate Interface
    * Plate Motion
    * Earthquake Data
* A**dded Colored Indicators to map**
    * Color depends on the magnitude of earthquake.
* **Tooltips**
    * Hovering over the circles will display information
* **Popup Information**
    * When user clicks on any one of the circle following information are displayed
        * Place of earthquake
        * Magnitude of earthquake which is color coded too
        * Date when the earthquake happened
        * Type information

![Map](img/earthquake.png)
#### Version 1.0
This is a basic visualization of earthquake in Indian Sub-Continent. The Blue markers shown in the map are places where the earthquake occured between 2010 to 2019.
![Map](img/earthquake_old.png)

## References
* [Modified Mercalli intensity scale](https://en.wikipedia.org/wiki/Modified_Mercalli_intensity_scale)
* [Magnitude / Intensity Comparison](https://earthquake.usgs.gov/learn/topics/mag_vs_int.php)
* [GIS Lounge](https://www.gislounge.com/find-tectonic-plate-gis-data/)
## Disclaimer
All data used in this example is sourced from internet. The Author does not take guarantee of accuracy.  


