from plotly import offline
from plotly.graph_objs import Bar,Layout

from die import Die

die_1 = Die()
die_2 = Die()
results = []
for roll_num in range(1000):
	result = die_1.roll()+die_2.roll()
	results.append(result)
# print(results)
max_num_sides = die_1.num_sides+die_2.num_sides
frequencies = []
for value in range(2,max_num_sides+1):
	frequence = results.count(value)
	frequencies.append(frequence)
# print(frequences)
x_values = list(range(2,max_num_sides+1))
data = [Bar(x=x_values,y=frequencies)]

x_axis_config = {'title':'结果'}
y_axis_config = {'title':'结果的频率'}
my_layout = Layout(title='投掷两个D6 1000次的结果',xaxis=x_axis_config,yaxis=y_axis_config)
offline.plot({'data':data,'layout':my_layout},filename='d6.html')