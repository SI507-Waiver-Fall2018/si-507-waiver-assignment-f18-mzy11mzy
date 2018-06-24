#name: Zhiyi Ma
#unique name: zhiyima
#umid: 48014433

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import csv

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets

py.sign_in('mzy11mzy', 'LO4P99WhpFkd39foTXTq')

noun_list = []
number_list = []
#with open('/Users/mazhiyi/Documents/GitHub/si-507-waiver-assignment-f18-mzy11mzy/noun_data.csv', 'r') as cfile:
with open('noun_data.csv', 'r') as cfile:
    csv_read = csv.reader(cfile)
    for a,b in csv_read:
        noun_list.append(a)
        number_list.append(b)

data = [go.Bar(x= noun_list[1:], y= number_list[1:])]
layout = go.Layout(title='Five most Commnon Nouns', barmode='stack', yaxis={'tickformat': ',d'})
fig = go.Figure(data=data, layout=layout)
py.image.save_as(fig, filename='part4_viz_image.png')
#py.image.save_as(fig, filename='/Users/mazhiyi/Documents/GitHub/si-507-waiver-assignment-f18-mzy11mzy/part4_viz_image.png')