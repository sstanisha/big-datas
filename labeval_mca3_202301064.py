import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import io
import seaborn as sns
data=pd.read_csv("company_sales.csv")
plt.bar(data["month_number"],data["facecream"],label="facecream")
plt.bar(data["month_number"],data["facewash"],label="facewash")
plt.xlabel('month')
plt.ylabel('sales')
plt.title("Bar chart")
plt.legend()
plt.show()
monthList= data['month_number'].tolist()
faceCremSalesData=data['facecream'].tolist()
faceWashSalesData=data['facewash'].tolist()
plt.bar([a-0.25 for a in monthList], faceCremSalesData, width= 0.25)
plt.bar([a+0.25 for a in monthList], faceWashSalesData, width= -0.25)
plt.xticks(monthList)
plt.xlabel('month list')
plt.ylabel('total sales')
plt.show()
