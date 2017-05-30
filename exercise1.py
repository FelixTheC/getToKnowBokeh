#! /usr/env/python3

import pandas
from bokeh.plotting import figure, output_file, show
location = r'verlegenhuken.xlsx'

df = pandas.read_excel(location, 0, index_col='Hour')
#df['Temperature'] = df.Temperature.apply(lambda x: x/10)
#df['Pressure'] = df.Pressure.apply(lambda x: x/10)
x_achse = df['Temperature']/10
y_achse = df['Pressure']/10

p = figure()

p.title = 'Temperature and Pressure'
p.title_text_color = 'grey'
p.xaxis.axis_label = 'Temperature (°C)'
p.yaxis.axis_label = 'Pressure (hPa)'

p.circle(x_achse, y_achse, size=0.5, color='blue')

output_file('pressureTemp.html')
show(p)