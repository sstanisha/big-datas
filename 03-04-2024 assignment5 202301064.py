#Q1 (i)
import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv('company_sales.csv')

plt.plot(data['total_profit'])

plt.title("Line chart")

plt.show()


#iii

import pandas as pd
import matplotlib.pyplot as plt
da=pd.read_csv('company_sales.csv')
plt.bar(da['facecream'],da['facewash'])
plt.bar(da['toothpaste'],da['bathingsoap'])
plt.bar(da['shampoo'],da['moisturizer'])
plt.title('Bar Chart')

plt.xlabel('category')
plt.ylabel('Sales')

plt.show()

        
#Q2
import plotly.express as px
import pandas as pd

data = {
    'X': [1, 2, 3, 4, 5],
    'Y': [2, 3, 4, 5, 6],
    'Label': ['A', 'B', 'C', 'D', 'E']
}

df = pd.DataFrame(data)

fig = px.scatter(df, x='X', y='Y', text='Label', title='Scatter Plot')

fig.show()

#Q3
import plotly.express as px
import pandas as pd
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Values': [10, 20, 15, 25, 30]
}
df = pd.DataFrame(data)
fig = px.bar(df, x='Category', y='Values', title='Bar Chart')
fig.show()

#Q4

import plotly.express as px
import pandas as pd

data = {
    'Numbers': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]
}
df = pd.DataFrame(data)
fig = px.histogram(df, x='Numbers', title='Histogram')
fig.show()

