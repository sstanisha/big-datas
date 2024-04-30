import pandas as pd
data=pd.read_csv('company_sales.csv')
print(data)

import matplotlib.pyplot as plt
#d=pd.read('facecream')
plt.bar('facecream','facecream')
plt.bar('facewash','facewash')
plt.show()
        
import matplotlib.pyplot as plt
month_number=[1,2,3,4,5,6,7,8,9,10,11,12]
total_profit=[
211000,
183300,
224700,
22700,
209600,
201400,
295500,
361400,
23400,
266700,
412800,
300200,
]
plt.hist('month_number','total_profit')
plt.show()
