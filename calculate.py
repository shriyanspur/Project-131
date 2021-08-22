import pandas as pd
import csv

df = pd.read_csv('final_data.csv')

headers = df[0]
data_rows = df[1:]

star_masses = []
star_radii = []
star_names = []
star_grav = []

for star_data in data_rows:
  star_radii.append(df[0])
  star_masses.append(df[8])
  star_radii.append(df[9])

for index, name in enumerate(star_names):
  grav = (float(star_masses[index])*5.972e+24)/(float(star_radii[index])*float(star_radii[index])*6371000*6371000)*6.674e-11
  star_grav.append(grav)