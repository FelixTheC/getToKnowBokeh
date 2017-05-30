#! /usr/env/python3

from bokeh.charts import Scatter, output_file, show
import pandas

df = pandas.DataFrame(columns=['X','Y'])
df['X'] = [1,2,3,4,5,6]
df['Y'] = [1,2,3,4,5,6]

p = Scatter(df, x='X', y='Y', title='Temperature Observation', xlabel='Day', ylabel='Temp')

output_file('Scatter_charts.html')

show(p)