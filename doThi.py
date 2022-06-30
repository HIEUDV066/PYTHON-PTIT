import pandas as pd
import matplotlib.pyplot as plt
import json

dictionary = json.load(open('metric.json', 'r'))
d = pd.read_json('metric.json')
print(d)
df1 = pd.DataFrame(d['Training Accuracy'])
df2 = pd.DataFrame(d['Valid Accuracy'])
df3 = pd.DataFrame(d['Train loss'])
df4 = pd.DataFrame(d['Valid loss'])
# dfg = df.groupby(d['Training Accuracy']).count()
# xAxis = [key for key, value in dictionary.items]
# yAxis = [value for key, value in dictionary.items()]

# ax = df1.plot(x='Step', y='Valid Accuracy')
ax = df1.plot(marker='o')
df2.plot(ax=ax, marker='s')
ax.set_xlabel("Epochs")
ax.set_ylabel("Accuracy")

ax1 = df3.plot(marker='o')
df4.plot(ax=ax1, marker='s')
ax1.set_xlabel("Epochs")
ax1.set_ylabel("Loss")

plt.show()
