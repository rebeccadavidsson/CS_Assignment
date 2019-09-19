import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(pd.read_csv("istherecorrelation.csv", delimiter = ";"))

plt.figure(dpi=300)
plt.plot(df["Year"], df["WO [x1000]"])
plt.show()
