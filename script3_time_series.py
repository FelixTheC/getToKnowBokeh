import pandas
from bokeh.plotting import figure, output_file, show

df = pandas.read_csv('adbe.csv', parse_dates=['Date'])

p = figure(width=800, height=600, x_axis_type='datetime')

p.line(df['Date'], df['Close'], color='orange', alpha=0.5)

output_file('series.html')
show(p)
