import geopandas as gpd
import folium
import mapclassify
from matplotlib import pyplot as plt 

file = gpd.read_file('file.shp')

m = file.explore('nom_colonne_a_affiche')
m