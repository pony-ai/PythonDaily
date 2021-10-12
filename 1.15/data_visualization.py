import matplotlib.pyplot as plt

# [
# 	'Solarize_Light2', 
# 	'_classic_test_patch',
# 	'bmh', 
# 	'classic', 
# 	'dark_background',
# 	'fast', 
# 	'fivethirtyeight', 
# 	'ggplot',
# 	'grayscale', 
# 	'seaborn',
# 	'seaborn-bright',
# 	'seaborn-colorblind',
# 	'seaborn-dark', 
# 	'seaborn-dark-palette',
# 	'seaborn-darkgrid', 
# 	'seaborn-deep', 
# 	'seaborn-muted', 
# 	'seaborn-notebook',
# 	'seaborn-paper', 
# 	'seaborn-pastel',
# 	'seaborn-poster',
# 	'seaborn-talk', 
# 	'seaborn-ticks',
# 	'seaborn-white', 
# 	'seaborn-whitegrid', 
# 	'tableau-colorblind10'
# ]
# input_value = [1,2,3,4,5]
# squares = [1,4,9,16,25]
input_value = range(1,1001)
# 列表解析
squares = [x**2 for x in input_value]
# print(squares)
plt.style.use('seaborn')

fig,ax = plt.subplots()
ax.scatter(input_value,squares,c='green',s=10)
# ax.plot(input_value,squares,linewidth=2)
ax.set_title("square",fontsize=24)
ax.set_xlabel("value",fontsize=14)
ax.set_ylabel("value*2",fontsize=14)

ax.tick_params(labelsize=10)
ax.axis([0,1100,0,1100000])
plt.show()