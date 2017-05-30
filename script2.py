#! /usr/env/python3

from bokeh.plotting import figure, show, output_file
import pandas

df = pandas.DataFrame(columns=['X','Y'])
df['X'] = [1,2,3,4,5,6]
df['Y'] = [2,4,6,8,10,1]

p = figure(plot_width=500, plot_height=500, title='title')

#p.circle([1,2,3,4,5,6], [2,4,6,8,10,1], size=6, color='red')
p.diamond([1,2,3,4,5,6], [2,4,6,8,10,1], size=16, color='red')

output_file('Scatter_plotts_2.html')

show(p)